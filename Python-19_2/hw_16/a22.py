s=input()
key=input()
keykey=[]
result=[]
length=len(key)
for i in range(len(s)):
    keykey.append(key[i%length])
for i in range(len(s)):
    if s[i]==" ":
        result.append(" ")
    elif ord(s[i])>ord(keykey[i]):
        result.append(chr(ord(s[i])-ord(keykey[i])+96))
    else:
        result.append(chr(ord(s[i])-ord(keykey[i])+122))
for i in result:
    print(i,end="")