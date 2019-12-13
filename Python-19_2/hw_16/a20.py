alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z'] # 알파벳 list

user_str = input()  # 입력받은 문장(평문)을 user_str에 저장
user_key = input() # 입력받은 문장(암호화 키)을 user_key에 저장

user_str_num = ""    # user_str의 알파벳 순서 저장할 변수 user_str_num 생성
new_key_num = ""    # user_key의 알파벳 순서 저장할 변수 user_key_num 생성


for i in range(0, len(user_str), 1):
    if user_str[i] == " ":  # user_str[i]가 " "이면 user_str_num에 " " 추가
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