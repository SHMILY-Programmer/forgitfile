from re import split

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rd

def setAxis():
    lent=range(-15,15,1)
    plt.xticks(lent)#横纵轴
    plt.yticks(lent)
    plt.plot([-18,18],[0,0],'k')
    plt.plot([0,0],[-18,18],'k')


def drawLine(st, ed,r='b'):#画线
    plt.plot([st[0],ed[0]],[st[1],ed[1]],r)

def calLRBT(site,line):
    d=line/2
    LRBT=[site[0]-d,site[0]+d,site[1]-d,site[1]+d]
    return LRBT


def drawBorder(LRBT):#裁剪边框
    x1=[LRBT[0],LRBT[2]]
    x2=[LRBT[1],LRBT[2]]
    x3=[LRBT[1],LRBT[3]]
    x4=[LRBT[0],LRBT[3]]
    print(x1,x2,x3,x4)
    drawLine(x1,x2,'k')
    drawLine(x1,x4,'k')
    drawLine(x2,x3,'k')
    drawLine(x3,x4,'k')

def calpoint(st, ed, LRBT):
    dx=ed[0]-st[0]
    dy=ed[1]-st[1]
    u0=[0]
    u1=[1]
    XL=LRBT[0]
    XR=LRBT[1]
    YB=LRBT[2]
    YT=LRBT[3]
    if ClipT(-dx,st[0]-XL,u0,u1):
        if ClipT(dx,XR-st[0],u0,u1):
            if ClipT(-dy,st[1]-YB,u0,u1):
                if ClipT(dy,YT-st[1],u0,u1):
                    s=[st[0]+u0[0]*dx,st[1]+u0[0]*dy]
                    print(s)
                    e=[st[0]+u1[0]*dx,st[1]+u1[0]*dy]
                    print(e)
                    drawLine(s,e,'r')


    print(u1[0])

def ClipT(p,q,u0,u1):
    if(p<0):
        r=q/p
        if r>u1[0]:
            print('s')
            return False
        if r>u0[0]:
            u0[0]=r
    if p>0:
        r=q/p
        if r<u0[0]:
            return False
        if r<u1[0]:
            u1[0]=r
    if p==0:
        return q>=0
    return True



if __name__=="__main__":
    setAxis()

    st=list(map(int,input("起点:").split()))
    ed=list(map(int,input("终点：").split()))
    border_site=list(map(int,input("方框中心:").split()))
    border_line=int((input("边长:")))
    dpx=ed[0]-st[0]
    dpy=ed[1]-st[1]
    drawLine(st,ed)
    LRBT=calLRBT(border_site,border_line)
    drawBorder(LRBT)
    calpoint(st,ed,LRBT)




    plt.show()
