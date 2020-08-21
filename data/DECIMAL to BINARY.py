
def dec_to_bin(dec_num):
    
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


print(dec_to_bin(800))  