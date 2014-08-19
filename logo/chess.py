from tealight.logo import move, turn, color

from random import choice 

word = choice (["code", "club"])

out =""

for letter in word:
  out = out + "_"
  
print("guess a letter in the word, then press enter:", out)

guess = input()

if guess in word:
  print("well done")
else:
    print("noooo")