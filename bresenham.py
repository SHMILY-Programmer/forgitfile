# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
def bresenhamline(x0,y0,x1,y1):
    dx=x1-x0
    dy=y1-y0
    k=dy/dx
    e=-0.5#初值
    x=x0
    y=y0
    xx=[]
    yy=[]
    plt.ion()
    plt.subplots()
    for i in range(0,dx+1):
        xx.append(x)
        yy.append(y)
        x=x+1
        e=e+k
        if e>=0:
            y+=1
            e-=1
        plt.scatter(xx,yy)
        plt.pause(1)
    plt.ioff()
    plt.show()
bresenhamline(0,0,5,2)

