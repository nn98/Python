# -*- coding: ms949 -*-

# Prefer//
# from ntpath import split
# remove=["\"","\'",".",",","!","?","(",")","\\"]
# words=input("word: ")
# print(words)
# for i in remove:
#     words=words.replace(i,"")
# words=words.split(" ")
# print(words)
# print("Number of word: %d" %len(words))

# ���ǻ��� : "word , word"�� ��� �ܾ��� ���� 2 �̴�.
# ������ �������� �ܾ �Ǻ��ϵ�, ���õ� Ư�����ڵ��� �����ϴ� ����
remove=["\"","\'",".",",","!","?","(",")","\\"] # ������ Ư�����ڵ�
words=input("����: ").lower()                    # ���� �Է�
for i in remove:                                # ������ Ư�����ڵ�
    words=words.replace(i,"")                   # ����
words=words.split(" ")                          # ������ �������� ����

# ����/���� �ܾ� ���ſ� �ڵ�
words.sort()                                    # ���ҵ� ����Ʈ�� ����
words=set(words)
count=0                                         # ���� ������ ���� 
for i in words:                                 # ''�� ���� ����
    if i != '':
        break
    count+=1
    
print("�ܾ��� ����: %d" %(len(words)-count))       # ���� ���� �ܾ� ���� ���