# -*- coding: ms949 -*-

"""
�Է��ϴ� ������ �ܾ��� ������ ����Ͻÿ�. ��ҹ��� ������ ���� �ʰ� ó���϶�.
��'.,!?()/ �� �ܾ �ƴϴ�.
�Է¿�)
����: While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
��¿�)
�ܾ��� ����:
"""
a=input("���� : ")  # �Է�
a=a.replace(",","")
a=a.replace(".","")
a=a.replace("\'","")
a=a.replace("\"","")
a=a.replace("?","")
a=a.replace("!","")
a=a.replace("/","")
a=a.replace("(","")
a=a.replace(")","") # �ܾ �ƴ� �͵��� �������� ��ü
a=a=a.lower() # ������ �ҹ��ڷ� �ٲ۴�.
word=[] # �ܾ �����ϱ� ���� list �� ������ �����Ѵ�.
for words in a.split(sep=' '):  # ������ �ܾ� ������ �ɰ���.
    word.append(words)  # �ܾ� ������ word �� �����Ѵ�.
word=list(set(word))    # �ߺ��� ������ ����Ʈ
print(word)
print("�ܾ��� ���� :",len(word)) # �ܾ��� ���� ���