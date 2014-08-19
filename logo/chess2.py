from tealight.logo import move, turn, color

>>> n = 3
>>> board = [["BW"[(i+j+n%2+1) % 2] for i in range(n)] for j in range(n)]
>>> print board
[['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]
>>> n = 4
>>> board = [["BW"[(i+j+n%2+1) % 2] for i in range(n)] for j in range(n)]
>>> print board
[['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W']]