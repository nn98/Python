str = input()   # �� �Է�
key_word = input()      # ��ȣ�� �Է�

count = len(str)    # ���ڿ� ����
result = list(range(count)) #���ڿ� ������ �´� ��ȣ������Ʈ �ʱ�ȭ

key = list(key_word * (count // len(key_word) + 1)) # ��ȣŰ �迭 �ʱ�ȭ

for i in result:       #��ȣȭ
    if str[i] != " ":   # ������ �ƴ� ���
        if ord(str[i]) <= ord(key[i]):      # ���ڰ� ��ȣ������ ���ų� �տ� ���� ���
            a = ord(str[i]) + 26 - ord(key[i]) + 96
            result[i] = chr(a)
        else:       # ���ڰ� ��ȣ�� ���� �ڿ� ���� ���
            a = ord(str[i]) - ord(key[i]) + 96
            result[i] = chr(a)
    else:       # ������ ���
        result[i] = str[i]

for i in result:    #��ȣ ���
    print(i,end="")
