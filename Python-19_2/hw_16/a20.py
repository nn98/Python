alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z'] # ���ĺ� list

user_str = input()  # �Է¹��� ����(��)�� user_str�� ����
user_key = input() # �Է¹��� ����(��ȣȭ Ű)�� user_key�� ����

user_str_num = ""    # user_str�� ���ĺ� ���� ������ ���� user_str_num ����
new_key_num = ""    # user_key�� ���ĺ� ���� ������ ���� user_key_num ����


for i in range(0, len(user_str), 1):
    if user_str[i] == " ":  # user_str[i]�� " "�̸� user_str_num�� " " �߰�
        user_str_num += " "
    else:
        for j in range(0, len(alpha), 1):
            if user_str[i] == alpha[j]:
                if i == len(user_str)-1:
                    user_str_num += (str(j+1))
                else:
                    user_str_num += (str(j+1) + " ")
str_num_list = user_str_num.split(" ")


length = len(user_str) % len(user_key)
new_key = user_key * (len(user_str)//len(user_key))

for i in range(0, length, 1):
    new_key += user_key[i]

for i in range(0, len(new_key), 1):
    for j in range(0, len(alpha), 1):
        if new_key[i] == alpha[j]:
            if i == len(new_key)-1:
                new_key_num += (str(j+1))
            else:
                new_key_num += (str(j+1) + " ")
key_num_list = new_key_num.split(" ")

result = ""

for i in range(0, len(str_num_list), 1):
    if str_num_list[i] == "":
        result += " "
    else:
        if str_num_list[i] >= key_num_list[i]:
            alpha_num_1 = int(str_num_list[i]) - int(key_num_list[i]) - int(1)
            result += alpha[alpha_num_1]
        else:
            alpha_num_2 = -1 * (int(key_num_list[i])-int(str_num_list[i])+int(1))
            result += alpha[alpha_num_2]

print(result)