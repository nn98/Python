def cipher(str, keyindex):
    """
    Vigenere cipher ����� ����� ���� ��ȣȭ�ϰ�, ��ȣ���� ��ȯ
    :param str: ��
    :param keyindex: ��ȣȭ Ű
    :return: ��ȣ��
    """
    k = ord(keyindex) - ord('a')+1
    s = ord(str) - ord('a')+1
    if s>k:
        p = ord('a')+(s-k)-1
    else:
        p = ord('z')-(k-s)
    return chr(p)

def count_reset(c,l):
    """
    ��ȣȭŰ�� �ݺ��ǵ��� index�� 1�� ������Ű�� index�� len(key)���� �Ǹ� �ʱ�ȭ
    :param c: �ε���
    :param l: ��ȣȭ Ű ����
    :return: �ε���
    """
    if c < l-1:
        c += 1
    else:
        c = 0
    return c

#���α׷� ����
str = input()   #�� �Է�
key = input()   #��ȣȭ Ű �Է�
lenkey = len(key)   #��ȣȭ Ű ����
count = 0   #��ȣȭ Ű �ε���

for i in str:
    if i == ' ':    #������ ���, ���� ���
        print(' ', end='')
        count = count_reset(count, lenkey)
    else:   #��ȣ�� ���
        print(cipher(i,key[count]), end='')
        count = count_reset(count, lenkey)