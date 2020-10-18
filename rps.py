import random, math

def Draw():
    print("We both picked the same.")
    return

def PWin():
    print("Well done you win.")
    return

def CWin():
    print("You lose.")
    return

StrUserType = input("Select Paper, Rock or Scissors (P,R or S)")
ComputerType = math.floor(random.random()*3)  #random.random(3)
# 0==Paper, 1==Rock and 2==Scissors

print("you picked ",StrUserType.upper())
print("The computer picked ",ComputerType)

if StrUserType.upper() == "P":
    if ComputerType == 0: Draw()
    elif ComputerType == 1: PWin()
    elif ComputerType == 2: CWin()
elif StrUserType.upper() == "R":
    if ComputerType == 1: Draw()
    elif ComputerType == 2: PWin()
    elif ComputerType == 0: CWin()
elif StrUserType.upper() == "S":
    if ComputerType == 2: Draw()
    elif ComputerType == 0: PWin()
    elif ComputerType == 1: CWin()
else:
    print("You need to pick a choice by typing the first letter only.")
    exit

