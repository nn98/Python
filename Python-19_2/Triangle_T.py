# -*- coding: ms949 -*-
from math import sqrt       #math 라이브러리에서 sqrt함수 가져옴

class Point :                       #Point 클래스
    def __init__(self,x,y):         #생성자
        self.x=x
        self.y=y

    def __str__(self):              #문자열 표현
        return "("+str(self.x)+","+str(self.y)+")"

    def getDistance(self,oth):      #두 점 거리 구하기
        return sqrt((self.x-oth.x)**2+(self.y-oth.y)**2)

class Triangle:                     #Triangle 클래스
    def __init__(self,p1,p2,p3):        #생성자
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def getHeight(self):            #높이 구하기
        return 2*self.getArea()/self.getWidth()

    def getWidth(self):             #폭 구하기
        return self.p1.getDistance(self.p2)

    def __str__(self):              #문자열 표현
        return str(self.p1)+str(self.p2)+str(self.p3)

    def getArea(self):              #넓이 구하기
        return sqrt(self.getLength()/2*(self.getLength()/2-self.p1.getDistance(self.p2))*(self.getLength()/2-self.p2.getDistance(self.p3))*(self.getLength()/2-self.p3.getDistance(self.p1)))

    def getLength(self):            #둘레 구하기
        return self.p1.getDistance(self.p2) + self.p2.getDistance(self.p3) + self.p3.getDistance(self.p1)


p1=Point(0,4)               #첫번째 점
p2=Point(3,4)               #두번째 점
p3=Point(0,0)               #세번째 점

t=Triangle(p1,p2,p3)        #삼각형 t 생성
print("삼각형의 세 점:",t)     #삼각형 출력(세 점)
print("높이:",t.getHeight())  #높이 출력
print("폭:",t.getWidth())     #폭 출력
print("넓이:",t.getArea())    #넓이 출력
print("둘레:",t.getLength())  #둘레 출력

