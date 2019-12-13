input_text=input()
input_key=input()
for i in range(len(input_text)):
    encord = input_key[i%len(input_key)] #인풋키는 키의 배열 수를 반복할 때마다 모듈러로 0부터 다시 시작한다.
    created_text=ord(input_text[i])-(ord(encord)-96) #만들어지는 텍스트는 인풋텍스트에 배열요소에서 인풋키의 배열요소에서
    #소문자 a가 시작하는 지점인 96만큼을 뺀 값을 빼준 값이다.
    if ord(input_text[i])!=32: #만약 입력된 텍스트가 공백이 아니고
         if  created_text < 97: # 생성된 텍스트가 a보다 작다면
             created_text += 26 # 거기에 다시 알파벳 갯수인 26을 더해 알파벳을 순환시키고
             print(chr(created_text), end='') #chr함수로 ord해준 것을 풀어준다.
         else:
             print(chr(created_text), end='') #만약 a보다 작지 않다면 빼준 값만 출력해준다.
    else:
        print(' ', end='') #32 즉 공백이 입력된 경우 그대로 공백을 입력해준다.
