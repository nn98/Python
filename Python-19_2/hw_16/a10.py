def trans(i, pi):
    if i == ' ': # �� ���ڿ��̸�
        return i # ��ȯ
    i = ord(i)
    for _ in range(ord(pi) - ord('a') + 1):
        i = i - 1
        if i == ord('a') - 1: # a�� �ƽ�Ű �ڵ� �� ���� 1 ������
            i = ord('z') # z�� �ƽ�Ű �ڵ� ������ ����
    return chr(i) # �ƽ�Ű �ڵ带 ���ڷ� �ٲپ ��ȯ

s = input() # �� �Է�
pk = input() # ��ȣȭ Ű �Է�
p = '' # ��ȣ������ ���� �� ���ڿ�
j = 0
for i in s:
    p = p + trans(i, pk[j])
    j = j + 1
    if j == len(pk):
        j = 0
print(p) # ��ȣ�� ���