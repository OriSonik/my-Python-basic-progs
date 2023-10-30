def decimal_to_binary(dec_num):
    index = 0
    while pow(2, index+1) <= dec_num:
        index += 1
    
    bin_num = ''
    
    for n in range(index,-1,-1):

        if pow(2, n) <= dec_num:
            bin_num = bin_num + '1'
            dec_num = dec_num - pow(2, n) 
        else:
            bin_num = bin_num + '0'
    return bin_num


def binary_to_decimal(bin_num):
    bin_num = bin_num[::-1]
    l = len(bin_num)
    dec_num = 0
    
    for index in range(l):
        dec_num += pow(2, index) * int(bin_num[index])
    
    
    return dec_num


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
