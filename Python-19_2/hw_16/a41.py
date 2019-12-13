"""
문제 백준 1718
풀이:
평문에 해당하는 각 알파벳과 키에 해당하는 각 알파벳의 번호를 알고 크기 비교를 한다. 평문에 공백문자가 있

평문과 키문의 알파벳 번호는 인덱스+1과 동일함, 따라서 인덱스+1 로 크기 비교하자. 그전에 공백문자인지 아닌지 검사

평문에 해당하는 알파벳 번호가 크다면 (평문 알파벳 크기 - 키 알파벳 크기), 평문 알파벳 번호가 더 작거나 서로 같다면
(결과값=평문 알파벳 크기 - 키 알파벳 크기), abs(결과값) 사용하여 양수화 하고 알파벳 역순 리스트 인덱스에서 인덱스+1과 비교하여
알파벳을 구하자
"""
alphabet=list("abcdefgfizklmnopqrstuvwxyz")  #알파벳 리스트화
rev_alphabet=list(reversed(alphabet))   #알파벳 역순 리스트

user=list(input())  #평문 입력 받기
key_ex=list(input())   #암호화 키 입력받기

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

for i in range(len(user)): #0부터 user 리스트 길이까지
    user_number=0 #해당 반복문 안에 존재해야하며, 매 반복시 초기화되어야 함
    key_number=0

    if user[i] != " ":  #평문의 요소가 공백문자인지 확인
        # 평문과 키문 요소의 알파벳 번호 구하기
        for al in alphabet: #평문과 키문의 요소가 어떤 알파벳과 동일한지 확인하기 위한 반복문
            if user[i] == al:
                user_number=alphabet.index(al)+1 #평문의 알파벳 번호를 구하여 저장
                #리스트.index(value)메소드는 리스트에 value값이 있으면 리스트에서의 value값의 위치를 반환, 없으면 오류
            if key[i] == al:
                key_number = alphabet.index(al) + 1 #키문의 알파벳 번호를 구하여 저장

        #평문과 키문의 알파벳 번호 비교하여 암호화 알파벳 찾기
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
