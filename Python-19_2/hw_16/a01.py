input_text=input()
input_key=input()
for i in range(len(input_text)):
    encord = input_key[i%len(input_key)] #��ǲŰ�� Ű�� �迭 ���� �ݺ��� ������ ��ⷯ�� 0���� �ٽ� �����Ѵ�.
    created_text=ord(input_text[i])-(ord(encord)-96) #��������� �ؽ�Ʈ�� ��ǲ�ؽ�Ʈ�� �迭��ҿ��� ��ǲŰ�� �迭��ҿ���
    #�ҹ��� a�� �����ϴ� ������ 96��ŭ�� �� ���� ���� ���̴�.
    if ord(input_text[i])!=32: #���� �Էµ� �ؽ�Ʈ�� ������ �ƴϰ�
         if  created_text < 97: # ������ �ؽ�Ʈ�� a���� �۴ٸ�
             created_text += 26 # �ű⿡ �ٽ� ���ĺ� ������ 26�� ���� ���ĺ��� ��ȯ��Ű��
             print(chr(created_text), end='') #chr�Լ��� ord���� ���� Ǯ���ش�.
         else:
             print(chr(created_text), end='') #���� a���� ���� �ʴٸ� ���� ���� ������ش�.
    else:
        print(' ', end='') #32 �� ������ �Էµ� ��� �״�� ������ �Է����ش�.
