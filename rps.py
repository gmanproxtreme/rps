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

if ComputerType == 0:
    print("The computer picked Paper")
    if StrUserType.upper() == "P": Draw()
    elif StrUserType.upper() == "R": CWin()
    elif StrUserType.upper() == "S": PWin()
elif ComputerType == 1:
    print("The computer picked Rock")
    if StrUserType.upper() == "P": PWin()
    elif StrUserType.upper() == "R": Draw()
    elif StrUserType.upper() == "S": CWin()
elif ComputerType == 2:
    print("The computer picked Scissors")
    if StrUserType.upper() == "P": CWin()
    elif StrUserType.upper() == "R": PWin()
    elif StrUserType.upper() == "S": Draw()
else:
    print("You need to pick a choice by typing the first letter only.")
    exit

