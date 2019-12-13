def code(a, b):
    if (a==' '): #공백 입력시
        return ' ' #공백 출력
    a1 = ord(a) - 97+1 #알파벳 소문자가 아스키코드 97부터 시작
    b1 = ord(b) - 97+1
    c = a1 - b1
    c = c+26
    c = c % 26
    if (c == 0): #만약 암호와 평문의 문자가 같다면
        c = 26 #z 출력
    return chr(96 + c)


a = input()
b = input()
list = []
for i in range(0,len(a)):
    list.append(code(a[i], b[i % len(b)]))
for i in range(0,len(a)):
    print(list[i], end='')