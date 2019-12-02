from math import *
from kandinsky import *

def draw_line(a,b,c,d,colore):
  if type(colore)==type(0):
    colore=color(colore,colore,colore)
  if a>c:
    tmp=a
    a=c
    c=tmp
    tmp=b
    b=d
    d=tmp
  if a-c==0:
    print(1)
    while b<d:
      set_pixel(a,b,colore)
      b=b+1
  else:
    ros=(b-d)/(a-c)
    if b<d:
      print(2)
      while b<d:
        set_pixel(round(a),round(b),colore)
        b=b+ros
        a=a+1
    else:
      print(3)
      ros=(a-c)/(b-d)
      while a<c:
        set_pixel(round(a),round(b),colore)
        b=b+1
        a=a+ros
