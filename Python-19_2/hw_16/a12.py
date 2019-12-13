s1=input("") #평문 입력받기 / 암호화할 문장
s2=input("") #암호화 키 입력 받기

dic={} #빈 딕셔너리 생성
chr=97 #97을 이용하여 소문자를 만드는 반복문에 사용할 예정
for x in range(1,27):
    dic[chr(chr)]=x
    chr=chr+1

a= len(s1)%len(s2) #암호화키를 평문의 길이에 맞추는 조건문에 쓰일 변수
if a!=0:
    for y in range(a):
        s2=s2+s2[y] #s1문자열 길이에 맞춰서 s2문자열 뒤에 s2문자열의
                    #s2[x]번째를 추가한다

F="" #최종 암호문을 출력하기위한 저장에 필요한 변수
for z in range(len(s1)):
    if s1[z]== " ": #s1[z]번째가 공백이면
        F=F+" "
        continue
    ori=dic.get(s1[z]) #평문숫자
    sec=dic.get(s2[z]) #암호문 숫자
    if ori> sec:
        F += chr(96 + ori - sec)
    else:
        temp = sec - ori
        F = F+ chr(122 - temp)
print(F)