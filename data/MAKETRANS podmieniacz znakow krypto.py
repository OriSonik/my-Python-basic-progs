intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)

str = "y tcpw sqcdsj rmmj"
print (str.translate(trantab))
