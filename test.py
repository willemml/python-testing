from math import *
from turtle import *
from kandinsky import *

hideturtle()
setheading(0)
points = []
exitprg = 0

def drawpoint(point):
  x=point[1]
  y=point[2]
  penup()
  goto(x-5,y)
  pendown()
  forward(9)
  penup()
  goto(x,y-5)
  pendown()
  left(90)
  forward(9)
  right(90)
  if x>0:
    x=160+x
  else:
    x=160-x*-1
  if y>0:
    y=111-y
  else:
    y=111+y*-1
  draw_string(point[0],x+6,y-18)

def draw_screen():
  for i in points:
    drawpoint(i[1],i[2],i[0])

def cmd():
  command = input("> ")
  if command == "h":
    print("Help menu:")
    print("h  - get to this menu")
    print("np - create a new point")
    print("nl - new line between points")
    print("rp - remove a point")
    print("ls - list existing points")
    print("dp - draw all points")
    print("dl - draw all lines")
    print("da - draw everything")
    print("exit or quit - quit this")
  if command == "np":
    print("Create a new point:")
    npointname = ""
    isnotdupe = 0
    while isnotdupe == 0:
      isnotdupe = 1
      npointname = input("NAME: ")
      for i in points:
        if npointname == i[0]:
          isnotdupe = 0
    npointx = input("XPOS: ")
    npointy = input("YPOS: ")
    points.append([npointname,npointx,npointy])
  if command == "nl":
    pointa = input("start point(0-" + str(len(points)-1) + "): ")
    pointb = input("end point(0-" + str(len(points)-1) + "): ")
  if command == "rp":
    print("Remove a point:")
    point = input("point number (0-" + str(len(points)-1) + "): ")
  if command == "lp":
    print("List of existing points:")
    for i in points:
      print("point '" + i[0] + "' x=" + str(i[1]) + " y=" + str(i[2]))
  if command == ("exit" or "quit"):
    exitprg=1


def main():
  print("Draw tool:")
  while exitprg==0:
    cmd()
  print("Goodbye.")
