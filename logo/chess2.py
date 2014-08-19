from tealight.logo import move, turn, color

def square(edges, size):
  angle = 360.0 / edges
  for i in range(1, edges):
    move(size)
    turn(angle)
    
square(10,100)