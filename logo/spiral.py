from tealight.logo import move, turn

def spiral(size):
  
  if size > 500:
    return
  
  move(size)
  turn(91)
  spiral(size + 5)
  
spiral(0)