str = input()   # 평문 입력
key_word = input()      # 암호문 입력

count = len(str)    # 문자열 개수
result = list(range(count)) #문자열 개수에 맞는 암호문리스트 초기화

key = list(key_word * (count // len(key_word) + 1)) # 암호키 배열 초기화

for i in result:       #암호화
    if str[i] != " ":   # 공백이 아닐 경우
        if ord(str[i]) <= ord(key[i]):      # 문자가 암호문보다 같거나 앞에 있을 경우
            a = ord(str[i]) + 26 - ord(key[i]) + 96
            result[i] = chr(a)
        else:       # 문자가 암호문 보다 뒤에 있을 경우
            a = ord(str[i]) - ord(key[i]) + 96
            result[i] = chr(a)
    else:       # 공백일 경우
        result[i] = str[i]

for i in result:    #암호 출력
    print(i,end="")
