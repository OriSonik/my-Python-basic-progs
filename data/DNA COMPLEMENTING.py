def dnaComplement(s):
    s = input('Enter a DNA structure, placing aminoacid symbols - A, C, T, G: ')
    s_rev = s.__reversed__()
        
        
    normal = 'ATCG'
    backwr = 'TAGC'
    s_rev_trans = s_rev.maketrans(normal, backwr)
    
    a = dnaComplement(s)
    return a
print()

       