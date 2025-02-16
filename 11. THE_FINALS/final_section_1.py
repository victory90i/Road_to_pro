# Question 1 : Write a program that accepts a sentence and calculate the number of upper
#  case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
# Hints: In case of input data being supplied to the question, it should be assumed to be
#  a console input.
s=input()
d={"UPPERCASE":0,"LOWERCASE":0}
for c in s:
  if c.isupper():
      d["UPPERCASE"]+=1
  elif c.islower():
      d["LOWERCASE"]+=1
  else:
      pass
print("UPPERCASE" ,d["UPPERCASE"])
print("LOWERCASE",d["LOWERCASE"])









# Question 2
# Question A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡
# ­ The numbers after the direction are steps. Please write a program to compute
#  the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program:
#  UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
import math
x=0
y=0
# # direction={
#     "UP":(0,1),
#     "DOWN":(0,-1),
#     "LEFT":(-1,0),
#     "RIGHT":(1,0)
# }
up=input("the direction up")
down=input("how many steps down")
left=input("how many steps left")
right=input("how many steps right")
y=int(up)-int(down)
x=int(left)-int(right)
pos=(x,y)

from_current_pos=math.sqrt(x**2 + y**2)
print(round(from_current_pos))

# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.