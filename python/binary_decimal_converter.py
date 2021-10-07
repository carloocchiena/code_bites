def bin_to_dec(digits):
    
    decimal = 0
    temp_bin_ints = []
    
    binary_raw = str(digits)
    binary = binary_raw[::-1]
    
    for i in binary:
        temp_bin_ints.append(int(i))
    
    for i in range(len(binary)):
        decimal += temp_bin_ints[i]*2**(i)
    
    return decimal
  
  def dec_to_bin(value):
    
    if value == 1:
        binary = "1"
    else:
        q = 0
        r = 0  
        binary_raw = []

        while int(value) > 1:
            value -= q+r
            q = value // 2
            r = value % 2
            binary_raw.append(r)

        binary_str = [str(int) for int in binary_raw]
        binary_inv = "".join(binary_str)
        binary = binary_inv[::-1]
    return binary
