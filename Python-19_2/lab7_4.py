# -*- coding: ms949 -*-

# Prefer//
# from ntpath import split
# remove=["\"","\'",".",",","!","?","(",")","\\"]
# words=input("word: ")
# print(words)
# for i in remove:
#     words=words.replace(i,"")
# words=words.split(" ")
# print(words)
# print("Number of word: %d" %len(words))

# 주의사항 : "word , word"의 경우 단어의 수는 2 이다.
# 공백을 기준으로 단어를 판별하되, 제시된 특수문자들을 제외하는 문제
remove=["\"","\'",".",",","!","?","(",")","\\"] # 삭제할 특수문자들
words=input("문장: ").lower()                    # 문장 입력
for i in remove:                                # 삭제할 특수문자들
    words=words.replace(i,"")                   # 삭제
words=words.split(" ")                          # 공백을 기죽으로 분할

# 공백/동일 단어 제거용 코드
words.sort()                                    # 분할된 리스트를 정렬
words=set(words)
count=0                                         # 개수 저장할 변수 
for i in words:                                 # ''의 개수 저장
    if i != '':
        break
    count+=1
    
print("단어의 개수: %d" %(len(words)-count))       # 공백 제외 단어 개수 출력