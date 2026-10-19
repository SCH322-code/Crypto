from Crypto.Util.number import *

with open('flag.txt','rb') as f:
    flag=f.read()

assert flag.startswith(b'VIDAR{') and flag.endswith(b'}')
plain=bytes_to_long(flag[6:-1])

assert plain.bit_length()<105
print(plain.bit_length())

a=[getPrime(233) for _ in range(105)]


bag=0

for i in a:
    temp=plain%2
    bag+=temp*i
    plain=plain>>1

print(f'{a=}')
print(f'{bag=}')

