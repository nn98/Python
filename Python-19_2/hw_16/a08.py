def s(a, key_a):  # �Լ� s �����ϱ�
    if a == ' ':  # �Է¹��� ���� �����̸�
        return a  # �׳� ��ȯ
    a = ord(a)  # ���� �ƽ�Ű�ڵ�� �ٲٱ�
    for i in range (ord(key_a)-ord('a')+1):  # ��ȣȭ Ű�� ���̸�ŭ ���ҽ�Ű��
        a -= 1  # �򹮿��� �ϳ��� ����
        if a == ord('a')-1:
            a = ord('z')
    return chr(a)

t = input()  # �� �Է�
k = input()  # ��ȣȭ Ű �Է�
l = len(k)  # ��ȣȭ Ű�� ����
i = 0
secret = ''
for a in t:
    secret += s(a, k[i])
    i += 1
    if i == l:
        i = 0
print(secret)