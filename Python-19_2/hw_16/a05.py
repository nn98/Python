import sys
sys.stdin=open("input.txt",'r')

def password=(a,key_a):
    if a==' ':
        return a
    a=ord(a)
    for _ in range(ord(key_a)-ord('a')+1):
        a=a-1
        if a==ord('a')-1:
            a=ord('z')
        return chr(a)
p=input()
key=input()
keylen=len(key)
i=0
cipher=''
for a in p:
    cipher+=password(a,key[i])
    i+=1
    if i==keylen:
        i=0
print(cipher)