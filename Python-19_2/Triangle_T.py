# -*- coding: ms949 -*-
from math import sqrt       #math ���̺귯������ sqrt�Լ� ������

class Point :                       #Point Ŭ����
    def __init__(self,x,y):         #������
        self.x=x
        self.y=y

    def __str__(self):              #���ڿ� ǥ��
        return "("+str(self.x)+","+str(self.y)+")"

    def getDistance(self,oth):      #�� �� �Ÿ� ���ϱ�
        return sqrt((self.x-oth.x)**2+(self.y-oth.y)**2)

class Triangle:                     #Triangle Ŭ����
    def __init__(self,p1,p2,p3):        #������
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def getHeight(self):            #���� ���ϱ�
        return 2*self.getArea()/self.getWidth()

    def getWidth(self):             #�� ���ϱ�
        return self.p1.getDistance(self.p2)

    def __str__(self):              #���ڿ� ǥ��
        return str(self.p1)+str(self.p2)+str(self.p3)

    def getArea(self):              #���� ���ϱ�
        return sqrt(self.getLength()/2*(self.getLength()/2-self.p1.getDistance(self.p2))*(self.getLength()/2-self.p2.getDistance(self.p3))*(self.getLength()/2-self.p3.getDistance(self.p1)))

    def getLength(self):            #�ѷ� ���ϱ�
        return self.p1.getDistance(self.p2) + self.p2.getDistance(self.p3) + self.p3.getDistance(self.p1)


p1=Point(0,4)               #ù��° ��
p2=Point(3,4)               #�ι�° ��
p3=Point(0,0)               #����° ��

t=Triangle(p1,p2,p3)        #�ﰢ�� t ����
print("�ﰢ���� �� ��:",t)     #�ﰢ�� ���(�� ��)
print("����:",t.getHeight())  #���� ���
print("��:",t.getWidth())     #�� ���
print("����:",t.getArea())    #���� ���
print("�ѷ�:",t.getLength())  #�ѷ� ���

