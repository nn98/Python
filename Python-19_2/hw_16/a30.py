"""
201914097 이가은 백준 1718번 문제 풀이
"""
s=list(input()) #평문 입력, 리스트에 넣는다
enc=list(input()) #암호화문 입력, 리스트에 넣는다
while 1: #참일 동안
    if len(enc)<len(s): #암호화 길이가 평문 길이보다 작으면
        enc+=enc #암호화 키에 해당 숫자를 더한다
    else: 
        break #아닐 경우 빠져 나온다
   
for i in range(len(s)): #평문의 길이 동안
    if s[i]==" ": #만약 공백이면
        continue #다시 돌아가서 다음으로 넘어간다
    else:
        z=ord(enc[i])-96 #암호화 인덱스문을 아스키코드로 변경한 후 96을 뺀다(97부터 소문자 시작)
        if ord(s[i])-z<97: #변형된 문자가 아스키코드로 a보다 작으면
            z-=26 #알파벳 상에서 맨 뒤로 숫자를 돌린다
        s[i]=chr(ord(s[i])-z) #아스키코드를 이제 문자로 변환한다
      
for i in range(len(s)): #평문이 끝날 때까지
    print(s[i],end="") #문자로 변환한 아스키코드를 출력한다
