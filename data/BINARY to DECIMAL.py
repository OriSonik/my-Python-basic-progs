def bin_to_dec(bin_num):
    bin_num = bin_num[::-1]
    l = len(bin_num)
    dec_num = 0
    
    for index in range(l):
        dec_num += pow(2, index) * int(bin_num[index])
    
    
    return dec_num
         
print(bin_to_dec('1110'))