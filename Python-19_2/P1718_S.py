n=input();k=input();r=''
j=-1
for i in n:
    j+=1
    if i==' ':r+=i
    else:r+=chr(122-(ord(k[j%len(k)])-ord(i))%26)
print(r)