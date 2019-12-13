def trans(i, pi):
    if i == ' ': # 빈 문자열이면
        return i # 반환
    i = ord(i)
    for _ in range(ord(pi) - ord('a') + 1):
        i = i - 1
        if i == ord('a') - 1: # a의 아스키 코드 값 보다 1 작으면
            i = ord('z') # z의 아스키 코드 값으로 변경
    return chr(i) # 아스키 코드를 문자로 바꾸어서 반환

s = input() # 평문 입력
pk = input() # 암호화 키 입력
p = '' # 암호문으로 만들 빈 문자열
j = 0
for i in s:
    p = p + trans(i, pk[j])
    j = j + 1
    if j == len(pk):
        j = 0
print(p) # 암호문 출력