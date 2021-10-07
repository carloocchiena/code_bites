"""
A Python native way to ping servers using Internet Control Message Protocol.

Did this an an homework assignement for the "Computer Networks: a top down approach"book.

Was not able to port it on Windows OS. Just Linux. 
"""

import socket
import os
import sys
import struct # Interpret bytes as packed binary data
import time
import select #this module is built for Solaris (UNIX OS). On Windows it just gives sockets support.
import binascii  

ICMP_ECHO_REQUEST = 8

def checksum(string): 
    '''Checksum
    This is based on the Two's complement operation, using bitwised operators, hex and ascii numbers.
    
    '''
    csum = 0
    count = 0
    count_to = (len(string) // 2) * 2  

    while count < count_to:
        this_val = ord(string[count+1]) * 256 + ord(string[count]) #using ord to convert characther to unicode integer value
        csum = csum + this_val 
        csum = csum & 0xffffffff  #hex for 4294967295 
        count = count + 2
    
    if count_to < len(string):
        csum = csum + ord(string[len(string) - 1])
        csum = csum & 0xffffffff 
    
    csum = (csum >> 16) + (csum & 0xffff) #bitwise right shift operator >>
    csum = csum + (csum >> 16)
    answer = ~csum #bitwise negation operator here for ~ 
    answer = answer & 0xffff #unsigned integer 65535
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer 
    
def receive_one_ping(my_socket, ID, timeout, dest_addr):
    time_left = timeout
    
    while True: 
        started_select = time.time()
        what_ready = select.select([my_socket], [], [], time_left)
        how_long_in_select = (time.time() - started_select)
        if what_ready[0] == []: # Timeout
            return "Request timed out."
    
        time_received = time.time() 
        #rec_packet, addr = my_socket.recvfrom(1024)
        rec_packet, addr = socket.recvfrom(1024) #Returns a bytes object read from an UDP socket and the address of the client socket as a tuple.
        
        # Fetch the icmp_header from the IP
        icmp_header = rec_packet[20:28]

        raw_TTL = struct.unpack("s", bytes([rec_packet[8]]))[0]  
        
        # binascii -- Convert between binary and ASCII  
        TTL = int(binascii.hexlify(raw_TTL), 16) 
        
        icmp_type, code, checksum, packet_ID, sequence = struct.unpack("bbHHh", icmp_header)
        
        if packet_ID == ID:
            byte = struct.calcsize("d") 
            time_sent = struct.unpack("d", rec_packet[28:28 + byte])[0]
            return "Reply from %s: bytes=%d time=%f5ms TTL=%d" % (dest_addr, len(rec_packet), (time_received - time_sent)*1000, TTL)
        
        time_left = time_left - how_long_in_select
        if time_left <= 0:
            return "Request timed out."

    
def send_one_ping(my_socket, dest_addr, ID):
    '''Header is type (8), code (8), checksum (16), id (16), sequence (16)'''
    
    my_checksum = 0
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.

    my_checksum = checksum(str(header + data)) 
    
    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order
        my_checksum = socket.htons(my_checksum) & 0xffff        
    else:
        my_checksum = socket.htons(my_checksum)
        
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    packet = header + data
    
    my_socket.sendto(packet, (dest_addr, 1)) 
    # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.
    
def do_one_ping(dest_addr, timeout): 
    icmp = socket.getprotobyname("icmp")

    # SOCK_RAW is a powerful socket type. For more details:   http://sock-raw.org/papers/sock_raw
    #AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with 
    #(in this case, Internet Protocol v4 addresses)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) 
    
    my_ID = os.getpid() & 0xFFFF  
    send_one_ping(my_socket, dest_addr, my_ID)
    delay = receive_one_ping(my_socket, my_ID, timeout, dest_addr)
    
    my_socket.close()
    return delay
    
def ping(host, timeout=1):
    '''Ping Function
    timeout=1 means: If one second goes by without a reply from the server,
    the client assumes that either the client's ping or the server's pong is lost
    '''
    dest = socket.gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    # Send ping requests to a server separated by approximately one second
    count = 0
    while count <= 10 :  
        delay = do_one_ping(dest, timeout)
        print(delay)
        time.sleep(1)# one second
        count +=1
    return delay
    
ping("localhost")
