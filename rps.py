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

if StrUserType.upper() == "P": 
    print("You picked Paper")
    if ComputerType == 0:
        print("The computer picked Paper")
        Draw()
    elif ComputerType == 1:
        print("The computer picked Rock")
        PWin()    
    elif ComputerType == 2:
        print("The computer picked Scissors")
        CWin()
elif StrUserType.upper() == "R": 
    print("You picked Rock")
    if ComputerType == 0:
        print("The computer picked Paper")
        CWin()
    elif ComputerType == 1:
        print("The computer picked Rock")
        Draw()    
    elif ComputerType == 2:
        print("The computer picked Scissors")
        PWin()
elif StrUserType.upper() == "S": 
    print("You picked Scissors")
    if ComputerType == 0:
        print("The computer picked Paper")
        PWin()
    elif ComputerType == 1:
        print("The computer picked Rock")
        Cwin()    
    elif ComputerType == 2:
        print("The computer picked Scissors")
        Draw()
else:
    print("You need to pick a choice by typing the first letter only.")