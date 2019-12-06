from math import *
from kandinsky import *

def dpl(a,b,max,bas,col,ros):
    if bas==0:
        while a<max:
            set_pixel(round(a),round(b),col)
            a=a+1
            b=b+ros
    elif baas==1:
        while b<max:
            set_pixel(round(a),round(b),col)
            a=a+ros
            b=b+1

def drawline(a,b,c,d,col):
    if d-b==0:
        s=[c,d,a,b]
        a=s[0]
        b=s[1]
        c=s[2]
        d=s[3]
    if type(col)==type(0):
        col=color(col,col,col)
    if (d-b>c-a or c-a==0) and d-b!=0:
        ros=(c-a)/(d-b)
        dpl(a,b,c,0,col,ros)
    elif c-a>d-b and c-a!=0:
        ros=(d-b)/(c-a)
        dpl(a,b,d,1,col,ros)
    else:
        print("incorrect")
