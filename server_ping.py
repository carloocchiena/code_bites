import socket

def ping_server(server: str, port: int, timeout=3):
    """Ping Server
    Ping the desidered server and port (such as "127.0.0.1", 8888) and return a bool value.
    
    """
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
    except OSError as error:
        return False
    else:
        s.close()
        return True

if __name__ == "__main__":
    print (ping_server("127.0.0.1", 8888))
