import random
print("Welcome to the rock paper scissors game",end="\n")

list=["rock","paper","scissor"]
print("Enter the following commands to indicate rock paper and scissor")
dic={
    1:"rock",
    2:"paper",
    3:"scissor",
}


print(dic)
guess=random.choice(list)


def userinput(x):
    index=list.index(guess)
    index=index+1
    if index==x:
        print("It's a tie.Computer's choice was ",guess)
    if index==1 and x==2:
        print("Congrats! You won. Computer's choice was",guess)   
    if index==1 and x==3:
        print("Oops! You lost.Computer's choice was",guess)  
    if index==2 and x==1:
        print("Oops!You lost.Computer's choice was",guess) 
    if index==2 and x==3:
        print("Congrats! You won.Computer's choice was",guess)
    if index==3 and x==1:
        print("Congrats!You won.Computer's choice was",guess)
    if index==3 and x==2:
        print("Oops! You lost.Computer's choice was",guess)                 


a=int(input("press 1,2 or 3:"))
if a<1 and a>3:
    print("Invalid input!Try again and enter only 1,2,or 3") 
else:
    userinput(a)