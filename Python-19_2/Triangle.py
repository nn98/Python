# -*- coding: ms949 -*-
"""
문제: 수업시간에 완성한 Point 클래스를 이용한다.
좌표평면상의 삼각형을 나타내는 Triangle 클래스를 정의한다.
3개의 Point를 매개변수로 받는 생성자
높이를 반환하는 getHeight
폭을 반환하는 getWidth
문자열을 반환하는 __str__ (세 점을 반환)
넓이를 반환하는 getArea
둘레를 반환하는 getLength

프로그램에서는
세 점을 만들고, 이 점들로 삼각형을 만든다.
삼각형을 출력한다.
삼각형의 높이, 폭, 넓이, 둘레를 출력한다.

작성자: 유수빈
작성일: 2019-11-27
"""
import math # sqrt라는 함수를 사용하기 위해

class Point:
    """
     좌표평면에 점을 나타내는 클래스
    """
    def __init__(self,x,y): # x,y좌표를 받는 생성자 메소드 정의
        self.x=x #self.을 붙이고 값을 지정하면 인스턴스 변수가 생성됨=x
        self.y=y#self.을 붙이고 값을 지정하면 인스턴스 변수가 생성됨=y
    def __str__(self): #문자열을 반환하는 메소드 정의
        return '('+str(self.x)+','+str(self.y)+')' #(x,y) 형태로 출력
    def getDistance(self,p): #두 점 사이의 거리를 반환하는 메소드 정의
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2) #두 점 사이의 거리 공식 사용


class Triangle(Point):
    """
    좌표평면상의 삼각형을 나타내는 클래스
    """
    def __init__(self,p1,p2,p3): # 3개의 Point를 매개변수로 가지는 메소드 정의
        self.p1=p1#self.을 붙이고 값을 지정하면 인스턴스 변수가 생성됨=p1=(x,y)
        self.p2=p2#self.을 붙이고 값을 지정하면 인스턴스 변수가 생성됨=p2=(x,y)
        self.p3=p3#self.을 붙이고 값을 지정하면 인스턴스 변수가 생성됨=p3=(x,y)
    def getWidth(self): #폭(밑변)을 구하는 메소드 정의
        return p1.getDistance(p2) #Point 클래스의 두 점 사이의 거리 사용/반환
    def getHeight(self):  # 높이를 구하는 메소드 정의
        h=abs(p3.y-p2.y) #점 p3의 y좌표에서 점 p2의 y좌표를 뺌
        return h # 높이 반환
    def __str__(self): # 문자열을 반환하는 메소드 정의
        return '('+str(self.p1)+','+str(self.p2)+','+str(self.p3)+')' #((,),(,),(,)) 형태로 출력
    def getLength(self): # 삼각형의 둘레를 구하는 메소드 정의
        a=p1.getDistance(p2) #점 p1과 점 p2 사이의 거리
        b=p2.getDistance(p3)#점 p2과 점 p3 사이의 거리
        c=p3.getDistance(p1)#점 p3과 점 p1 사이의 거리
        Length = a+b+c # 둘레=각각의 거리를 다 더함
        return Length # 둘레 반환
    def getArea(self): # 삼각형의 넓이를 구하는 메소드 정의
        area=p1.getDistance(p2)*abs(p3.y-p2.y)/2 #넓이=밑변*높이/2
        return area # 넓이 반환

#프로그램 시작
p1=Point(3,5) # 첫번째 점 설정
p2=Point(-2,5) # 두번째 점 설정
p3=Point(6,0) # 세번째 점 설정

p=Triangle(p1,p2,p3) #Triangle 클래스로 3개의 점 반환 설정
print(p) # ((,),(,),(,)) 형식으로 출력(__str__출력)

# 삼각형이 어떤 삼각형인지 정해져 있지 않아 ,점과 점사이의 거리에서 루트가 나올 수 있어서
# %.1d로 소수점 이하를 제거하려 했으나, 원래 값을 쓰는 게 맞는 것 같아서 수정 안함.
print('폭:',p.getWidth())
print('높이:',p.getHeight())
print('둘레:',p.getLength())
print('넓이:',p.getArea())


"""
루트로 인해 둘레나 넓이가 소수점 아래로 많이 나와서 소수점 이하 생략한 부분의
출력을 두번째 방법으로 써놓음.
print('폭:%.1d'%p.getWidth())
print('높이:%.1d'%p.getHeight())
print('둘레:%.1d'%p.getLength())
print('넓이:%.1d'%p.getArea())
"""