"""
ฐ๛ผ๖มพ
"""
a=input()
key=input()
d=[]
b=[]
dic='abcdefghijklmnopqrstuvwxyz'
c=len(a)%len(key)
for x in range(len(a)):
    for i in dic:
        if a[x] == ' ':
            b.append(' ')
            break
        elif a[x] == i:
            b.append(dic.index(i))
for w in range(len(key)):
    for y in dic:
        if key[w] == y:
            d.append(dic.index(y))
if c == 0 :
    k=int(len(a)/len(key))*d
    for s in range(len(a)):
        if b[s] ==' ' :
            print(' ',end="")
        else:
            print(dic[b[s]-k[s]-1],end="")
else:
    k=int(len(a)/len(key))*d
    for t in range(c):
        k.append(dic.index(key[t]))

    for s in range(len(a)):
        if b[s] ==' ' :
            print(' ',end="")
        else:
            print(dic[b[s]-k[s]-1],end="")