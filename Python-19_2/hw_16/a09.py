sentence1 = input()#��
sentence2= input()#��ȣ�� �򹮿���  ��ȣȭ�� ���ڰ��� ���� �� ������ �� ���׸�ŭ ���ߵ�
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
    py     = dic.get(sentence1[y])#dic�� �ش��ϴ� �򹮼���
    secret = dic.get(sentence2[y])# ��ȣ�� ����
    if py>secret:
        final+=chr(96+py-secret)
    else:
        temp = secret-py
        final+=chr(122-temp)
print(final)  