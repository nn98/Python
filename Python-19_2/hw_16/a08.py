def s(a, key_a):  # 함수 s 정의하기
    if a == ' ':  # 입력받은 평문이 공백이면
        return a  # 그냥 반환
    a = ord(a)  # 평문을 아스키코드로 바꾸기
    for i in range (ord(key_a)-ord('a')+1):  # 암호화 키의 길이만큼 감소시키기
        a -= 1  # 평문에서 하나씩 감소
        if a == ord('a')-1:
            a = ord('z')
    return chr(a)

t = input()  # 평문 입력
k = input()  # 암호화 키 입력
l = len(k)  # 암호화 키의 길이
i = 0
secret = ''
for a in t:
    secret += s(a, k[i])
    i += 1
    if i == l:
        i = 0
print(secret)