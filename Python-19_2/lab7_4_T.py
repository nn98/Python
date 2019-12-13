# -*- coding: ms949 -*-

"""
입력하는 문장의 단어의 개수를 출력하시오. 대소문자 구별을 하지 않게 처리하라.
“'.,!?()/ 는 단어가 아니다.
입력예)
문장: While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
출력예)
단어의 개수:
"""
a=input("문장 : ")  # 입력
a=a.replace(",","")
a=a.replace(".","")
a=a.replace("\'","")
a=a.replace("\"","")
a=a.replace("?","")
a=a.replace("!","")
a=a.replace("/","")
a=a.replace("(","")
a=a.replace(")","") # 단어가 아닌 것들은 공백으로 대체
a=a=a.lower() # 문장을 소문자로 바꾼다.
word=[] # 단어를 저장하기 위해 list 형 변수를 생성한다.
for words in a.split(sep=' '):  # 문장을 단어 단위로 쪼갠다.
    word.append(words)  # 단어 단위를 word 에 저장한다.
word=list(set(word))    # 중복을 제외한 리스트
print(word)
print("단어의 개수 :",len(word)) # 단어의 개수 출력