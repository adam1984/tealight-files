from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

print "This is art mode!"

print screen_width
print screen_height

background("paper.jpg")

line(0,0,screen_width, screen_height)

spot(200,300, 20)

circle(300,200, 20)

box(500, 500, 60, 60)

image(200,200,"bird.png")

line(560,0,560,495)

text(600, 100, "Hello Adam!")

lastx = None
lasty = None
hue = 0

def handle_mousemove(x,y):
  global lastx, lasty, hue
  
  line(lastx or x, lasty or y, x, y)
  circle(lastx or x, lasty or y, x)
  
  #color("hsl(%d,100%%,50%%)" % hue)
  color("rgba(400,9,0,0.7)" % hue)
  
  box(lastx or x, lasty or y, x, y)
  
  #spot(lastx or x, lasty or y, x)
  #color("hsl(%d,100%%,50%%)" % hue)
  
  hue += 1
 
  
  lastx = x
  lasty = y
  

  
