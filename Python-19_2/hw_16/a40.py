alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',

         'w', 'x', 'y', 'z']#알파벳정의
a_num=""#공백
b_num=""
a=input()
b=input()


for i in range(0, len(a), 1):
    if a[i] == " ":
        a_num += " "
    else:
        for j in range(0, len(alp), 1):
            if a[i] == alp[j]:
                if i == len(a) - 1:
                    a_num += str(j)
                else:
                    a_num += (str(j) + " ")

a_num_list = a_num.split(" ")

length = len(a) % len(b)
new_b = (len(a)//len(b)) * b

for i in range(0, length, 1):
    new_b += b[i]

for i in range(0, len(new_b), 1):
    for j in range(0, len(alp), 1):
        if new_b[i] == alp[j]:
            if i == len(new_b)-1:
                b_num += (str(j))
            else:
                b_num += (str(j) + " ")
b_num_list = b_num.split(" ")

result = ""

for i in range(0, len(a_num_list), 1):
    if a_num_list[i] == "":
        result += " "
    else:
        if a_num_list[i] <= b_num_list[i]:
            alphabet2 = -1 * (int(b_num_list[i])-int(a_num_list[i]) + int(1))
            result += alp[alphabet2]

        else:
            alphabet1 = int(a_num_list[i]) - int(b_num_list[i]) - int(1)
            result += alp[alphabet1]


print(result)