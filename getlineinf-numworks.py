from calcline import *
from drawline import *

def line():
  print("Welcome to line info!")
  xa=float(input("enter Xa: ")
  ya=float(input("enter Ya: ")
  xb=float(input("enter Xb: ")
  yb=float(input("enter Yb: ")
  print("y at x0 (p): ",str(getlinep(xa,ya,xb,yb))
  print("y-p at x1 (m): ",str(getlinem(xa,ya,xb,yb))
  draw_line(160+xa,111-ya,160+xb,111-yb)
