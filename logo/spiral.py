from tealight.logo import move, turn

def spiral(size):
  
  if size > 100:
    return
  
  move(size)
  turn(90)
  spiral(size + 1)
  
spiral(0)