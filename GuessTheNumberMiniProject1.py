import random

randNum=random.randint(1,100)
# print(randNum)
y=0
print("You get 7 chances to GUESS THE CORRECT NUMBER")
print("HINT: NUmber lies between 1 to  100!!!")
while(y<7):
  x=int(input("Guess the number.."))
 
  if x==randNum:
    print("YOU GUESSED IT RIGHT!!👑👑")
    break
  elif x<randNum-10:
    print("You are near to the Number go plus plus")
    pass
  elif randNum-10<=x<=randNum+10:
    print("You are almost there")
    pass
  elif  x>randNum+10:
    print("you are too far from the Number go minus minus")
  elif randNum>100:
    print("Out of range")       
y+=1