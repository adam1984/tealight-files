from tealight.art import fill_polygon
from math import sin, cos, pi

def triangle(x,y,size):
  x0 = x + size* sin(0)
  y0 = y + size* cos(0)
  x1 = x + size* sin(2*pi/3)
  y1 = y + size* cos(2*pi/3)
  x2 = x + size* sin(2* 2*pi/3)
  y2 = y + size* cos(2* 2*pi/3)
  
  fill_polygon([(x0,y0),(x1,y1),(x2,y2)])

triangle(50,50,50) 

triangle.rotate(angle=pi/4, axis=axis, origin=pos)
radians(360) is equal to 2*pi
degrees(2*pi) is equal to 360


def triangle2(x,y,size):
  x0 = x + size* sin(0)
  y0 = y + size* cos(0)
  x1 = x + size* sin(2*pi/3)
  y1 = y + size* cos(2*pi/3)
  x2 = x + size* sin(2* 2*pi/3)
  y2 = y + size* cos(2* 2*pi/3)
  
  fill_polygon([(x0,y0),(x1,y1),(x2,y2)])

triangle2(150,150,20) 
