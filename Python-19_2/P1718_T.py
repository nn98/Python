# -*- coding: ms949 -*-
alphabet=list("abcdefgfizklmnopqrstuvwxyz")  #���ĺ� ����Ʈȭ
rev_alphabet=list(reversed(alphabet))   #���ĺ� ���� ����Ʈ

user=list(input())  #�� �Է� �ޱ�
key_ex=list(input())   #��ȣȭ Ű �Է¹ޱ�

key=[]

if len(user) == len(key_ex):
    key+=key_ex
elif len(user) > len(key_ex):
    tempo=len(user) // len(key_ex)
    key=key_ex * tempo

    if len(user) % len(key_ex) != 0:
        for i in range(len(user) % len(key_ex)):
            key.append(key_ex[i])
else:
    for user_len in range(len(user)):
        key.append(key_ex[user_len])

for i in range(len(user)): #0���� user ����Ʈ ���̱���
    user_number=0 #�ش� �ݺ��� �ȿ� �����ؾ��ϸ�, �� �ݺ��� �ʱ�ȭ�Ǿ�� ��
    key_number=0

    if user[i] != " ":  #���� ��Ұ� ���鹮������ Ȯ��
        # �򹮰� Ű�� ����� ���ĺ� ��ȣ ���ϱ�
        for al in alphabet: #�򹮰� Ű���� ��Ұ� � ���ĺ��� �������� Ȯ���ϱ� ���� �ݺ���
            if user[i] == al:
                user_number=alphabet.index(al)+1 #���� ���ĺ� ��ȣ�� ���Ͽ� ����
                #����Ʈ.index(value)�޼ҵ�� ����Ʈ�� value���� ������ ����Ʈ������ value���� ��ġ�� ��ȯ, ������ ����
            if key[i] == al:
                key_number = alphabet.index(al) + 1 #Ű���� ���ĺ� ��ȣ�� ���Ͽ� ����

        #�򹮰� Ű���� ���ĺ� ��ȣ ���Ͽ� ��ȣȭ ���ĺ� ã��
        if user_number > key_number:
            new_code_number=(user_number-key_number)-1
            print(alphabet[new_code_number], end="")
        elif user_number < key_number:
            new_code_number=abs(user_number-key_number)
            print(rev_alphabet[new_code_number], end="")
        else:
            print("z", end="")
    else:
        print(" ", end="")