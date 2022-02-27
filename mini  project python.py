
import random
n=int(input("Number of games you want to play........"))
lst=["rock","paper","scissor"]

up=0
sp=0
tie=0


for i in range(n):
    print(lst)
    user=input("Enter ur choise ......")
    if user not in lst:
        print("Enter valid input from",lst)
        user=input("Enter ur choise ......")
    system=random.choice(lst)
    print("system choice", system)
    if user==system:
        print("game tie")
        tie+=1
    elif user=="rock":
        if system=="scissor":
            print("User won the round")
            up+=1
        else:
            print("system won the round")
            sp+=1
    elif user=="paper":
        if system=="scissor":
            print("system won the round")
            sp+=1
        else:
            print("User won the round")
            up+=1
    elif user=="scissor":
        if system=="paper":
            print("User won the round")
            up+=1
        else:
            print("system won the round")
            sp+=1
if up>sp:
    print("Congrats!!! ")
    print("User won the game")
elif up==sp:
    print("Game tie ")
    print("Try again ")
else:
    print("Better luck next time ")
    print("system won the game")
    
print("User point=",up)
print("System point=",sp)
print("Tied games=",tie)

