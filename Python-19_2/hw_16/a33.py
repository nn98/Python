def encrypt(i, o_i):
    if i ==" ":
        return i
    i = ord(i)
    for j in range(ord(o_i)-ord('a')+1):
        i -= 1
        if i == ord('a')-1:
             i == ord('z')
    return chr(i)

p=input()
o=input()
olen=len(o)
oidx=0
cipher=''

for i in p:
    cipher += encrypt(i,o[oidx])
    oidx += 1
    if oidx == olen:
        oidx = 0
print(cipher)