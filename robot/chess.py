from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code heredef spiral(size):
  
  if size > 500:
    return
  
  move(size)
  turn(90)
  spiral(size + 5)
  
spiral(0)