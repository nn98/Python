def code(a, b):
    if (a==' '): #���� �Է½�
        return ' ' #���� ���
    a1 = ord(a) - 97+1 #���ĺ� �ҹ��ڰ� �ƽ�Ű�ڵ� 97���� ����
    b1 = ord(b) - 97+1
    c = a1 - b1
    c = c+26
    c = c % 26
    if (c == 0): #���� ��ȣ�� ���� ���ڰ� ���ٸ�
        c = 26 #z ���
    return chr(96 + c)


a = input()
b = input()
list = []
for i in range(0,len(a)):
    list.append(code(a[i], b[i % len(b)]))
for i in range(0,len(a)):
    print(list[i], end='')