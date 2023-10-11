import random
list_item=["Rock","Paper","Scissor"]

user_choice=input("your choice = Rock, Paper, Scissor = ")
comp_choice=random.choice(list_item)

print(user_choice,comp_choice)

if user_choice==comp_choice:
    print("Match tie")

elif user_choice=="Rock":
    if user_choice=="Paper":
        print("Paper covers Rock, Computer wins")
    else:
        print("Rock smashes Scissor, You Won")

elif user_choice=="Paper":
    if user_choice=="Scissor":
        print("Scissor cuts Paper, Computer Wins")
    else:
        print("Paper covers Rock, You Won")
elif user_choice=="Scissor":
    if user_choice=="Rock":
        print("Rock smashes Scissor, Computer won")
    else:
        print("Scissor cuts Paper, You won")