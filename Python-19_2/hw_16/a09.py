sentence1 = input()#평문
sentence2= input()#암호문 평문에서  암호화의 숫자값을 뺐을 때 음수면 그 차액만큼 빼야됨
dic = {}
final=""
i=97
j=0
sen=''



for x in range(len(sentence1)):
    if x%len(sentence2)==0:
        j=0
        sen+=sentence2[j]
        j+=1
    else:
        sen+= sentence2[j]
        j+=1
sentence2=sen

for x in range(1,27):
    dic[chr(i)]=x#a=1, b=2...
    i+=1

    
for y in range(len(sentence1)):
    if sentence1[y]==" ":
        final+=" "
        continue
    py     = dic.get(sentence1[y])#dic에 해당하는 평문숫자
    secret = dic.get(sentence2[y])# 암호문 숫자
    if py>secret:
        final+=chr(96+py-secret)
    else:
        temp = secret-py
        final+=chr(122-temp)
print(final)  