s1=input("") #�� �Է¹ޱ� / ��ȣȭ�� ����
s2=input("") #��ȣȭ Ű �Է� �ޱ�

dic={} #�� ��ųʸ� ����
chr=97 #97�� �̿��Ͽ� �ҹ��ڸ� ����� �ݺ����� ����� ����
for x in range(1,27):
    dic[chr(chr)]=x
    chr=chr+1

a= len(s1)%len(s2) #��ȣȭŰ�� ���� ���̿� ���ߴ� ���ǹ��� ���� ����
if a!=0:
    for y in range(a):
        s2=s2+s2[y] #s1���ڿ� ���̿� ���缭 s2���ڿ� �ڿ� s2���ڿ���
                    #s2[x]��°�� �߰��Ѵ�

F="" #���� ��ȣ���� ����ϱ����� ���忡 �ʿ��� ����
for z in range(len(s1)):
    if s1[z]== " ": #s1[z]��°�� �����̸�
        F=F+" "
        continue
    ori=dic.get(s1[z]) #�򹮼���
    sec=dic.get(s2[z]) #��ȣ�� ����
    if ori> sec:
        F += chr(96 + ori - sec)
    else:
        temp = sec - ori
        F = F+ chr(122 - temp)
print(F)