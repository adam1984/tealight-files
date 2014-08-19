from tealight.logo import move, turn

def square(edges, size):
  angle = 360.0 / edges
  
  for i in range(0, edges):
    move(size)
    turn(angle)
    
square(4,50)

 for y in range(5, edges):
    move(size)
    turn(angle)

square(4,100)
    