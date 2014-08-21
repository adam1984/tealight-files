from tealight.art import box,line_width,polygon,color,fill_polygon,clear,screen_width,screen_height
from math import sin, cos, pi
from tealight.utils import sleep


def triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
    
  polygon(pts)

def fill_triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
    
  fill_polygon(pts)
  

m_a = 0

line_width(3)
def handle_frame():
  global m_a
  
  color("white")
  box(0,0,screen_width,screen_height)
  
  for i in range(0,25,1):
    color("hsl(0,100%," + str(i*4) + "%)")
    fill_triangle(150,100,200-i*6,2*i*m_a)
  
    color("hsl(0,100%," + str(i*4-20) + "%)")
    triangle(200,200,200-i*6,2*i*m_a)
    
  m_a += 0.002
  
  sleep(30)