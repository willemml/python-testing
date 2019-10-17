from math import *
from turtle import *
from kandinsky import *

speed(10)
hideturtle()
setheading(0)
points = []
lines = []
exitprg = 0

def drawline(line):
  xa=-160+line[0]
  ya=-110+line[1]
  xb=-160+line[2]
  yb=-110+line[3]
  penup()
  goto(xa,ya)
  pendown()
  goto(xb,yb)
  penup()

def drawpoint(point):
  x=-160+point[1]
  y=-110+point[2]
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
  draw_string(point[0],point[1]+6,223-point[2]-18)

def cmd():
  command = input("> ")
  if command == "h":
    print("Help menu:")
    print("h  - get to this menu")
    print("np - create a new point")
    print("nl - new line between points")
    print("rp - remove a point")
    print("lp - list existing points")
    print("ll - list existing lines")
    print("dp - draw all points")
    print("dl - draw all lines")
    print("da - draw everything")
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
    npointx = int(input("XPOS: "))
    npointy = int(input("YPOS: "))
    points.append([npointname,npointx,npointy])
  if command == "nl":
    name = ""
    isnotdupe = 0
    while isnotdupe == 0:
      isnotdupe = 1
      name = input("NAME: ")
      for i in lines:
        if name == i[3]:
          isnotdupe = 0
    a = int(input("start point(0-" + str(len(points)-1) + "): "))
    b = int(input("end point(0-" + str(len(points)-1) + "): "))
    c = [points[b][1] - points[a][1], points[b][2] - points[a][2]]
    ab = sqrt((points[b][1]-points[a][1])^2+(points[b][2]-points[a][2])^2)
    lines.append([points[a][1], points[a][2], points[b][1], points[b][2], length, name])
  if command == "dp":
    for i in points:
      drawpoint(i)
    keyhasbeenpressed = 0
    while keyhasbeenpressed == 0:
      if len(get_keys()) > 0:
        keyhasbeenpressed = 1
  if command == "ll":
    print("command not yet created")
  if command == "da":
    print("command not yet created")
  if command == "dl":
    print("command not yet created")
  if command == "rp":
    print("Remove a point:")
    point = int(input("point number (0-" + str(len(points)-1) + "): "))
    print("Is this right?")
    print(str(point) + ". point '" + str(points[point][0]) + "' x=" + str(points[point][1]) + " y=" + str(points[point][2]))
    yesno = input("[y/n] > ")
    if yesno == "y":
      points.pop(point)
    if yesno == "n":
      cmd()
  if command == "lp":
    print("List of existing points:")
    pnum = 0
    for i in points:
      print(str(pnum) + ". point '" + i[0] + "' x=" + str(i[1]) + " y=" + str(i[2]))

def main():
  print("Draw tool:")
  while exitprg == 0:
    cmd()
