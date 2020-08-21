def perfectTeam(skills):
    p = int(skills.count('p'))
    c = int(skills.count('c'))
    m = int(skills.count('m'))
    b = int(skills.count('b'))
    z = int(skills.count('z'))

    if p >= 1 and c >= 1 and m >= 1 and b >= 1 and z >= 1:
        sum = p + c + m + b + z
        for sum in range (5, pow(10,5)+1):
            my_list = [p, c, m, b, z]
            x = min(i for i in my_list)
            return x
    
    print(x)
perfectTeam('pcmbz')