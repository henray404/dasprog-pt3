# DILARANG MENGGUNAKAN IMPORT LIBRARY, JIKA MENGGUNAKAN MAKA AKAN DIANGGAP SALAH!

a, b = map(int, input().split())

if a % b == 0:
    c = b
else:
    c = a
d = (a*b)//c

output = ((c*d//a) + (c*d//b))
print(output)
