from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "yellow"]

for i in range(20,50,10,20):
  move(i)
  turn(90)
  color(colors[i%3])