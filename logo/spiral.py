from tealight.logo import move, turn

def spiral(size):
  
  if size > 700:
    return
  
  move(size)
  turn(91)
  spiral(size + 1)
  
spiral(0)