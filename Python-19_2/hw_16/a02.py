text=input() # ��
co=input() # ��ȣ

text_num=[] # ���� ����(0~25)�� ���� ����Ʈ
co_num=[] # ��ȣ�� ����(1~26)�� ���� ����Ʈ
answer=[] # ������ ���� ����Ʈ

for i in co:        # ��ȣ�� �ϳ��� �ƽ�Ű�ڵ�� �޾� 96�� ����(a=97�̱� ����).
    co_num.append(ord(i)-96)

for i in text:      # ���� �ϳ��� �ƽ�Ű�ڵ�� �޾� 97�� ����. ������ ��� ������ �״�� �ִ´�.
    if i!=' ':
        text_num.append(ord(i)-97)
    else:
        text_num.append(i)

while len(co_num)<len(text_num): # ��ȣ�� �򹮺��� ª�� ���, ��ȣ�� ���̸� �ø���.
    co_num+=co_num

for i in range(len(text_num)):          # �򹮰� ��ȣ�� �ϳ��� �����ؼ� �򹮼���-��ȣ���� ����
    if text_num[i]!=' ':                # �׸��� 26���� ���� �������� answer_num���� ����
        answer_num=(text_num[i]-co_num[i])%26 # (a�� ��� 0%26=0, b�� 1%26=1...-1�� ����
        answer.append(chr(answer_num+97))     # -1%26=25 �̹Ƿ� z�� �ȴ�.)
    else:
        answer.append(' ')
print(''.join(answer))      # answer ����Ʈ�� ���ڿ��� �����ؼ� ���