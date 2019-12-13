# -*- coding: ms949 -*-
# 11/21 13:30
word=input()
code=input()
nowC=-1
R=''
for i in word:
    nowC+=1
    if i==' ':
        R+=i
        continue;
    w=ord(i)-97
    c=ord(code[nowC%len(code)])-96
    p=w-c
    if p<0:
        r=chr(123+p)
    else:
        r=chr(97+p)
    R+=r
print(R)