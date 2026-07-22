# snake water gun game
# snake drinks water, water drowns gun, gun kills snake

import random

choice=["water","snake","gun"]


rules={
    ("snake","water"):"snake drinks water",
    ("water","gun"):"water drowns gun",
    ("gun","snake"):"gun kills snake"
}
print("Welcome to the snake-water-gun game")
print("The rules are:")
for key,value in rules.items():
    print(f"{key[0]} vs {key[1]} --> {value}")

print("\nEnter either snake,water or gun:\n")

def yourchoice(x):
        if(x==computerchoice):
            print(f"It's a draw. Computer's choice was also {computerchoice}")
        
        elif(x,computerchoice)in rules:
            print(f"Congrats! You win.Computer's choice was {computerchoice}" )
        elif(computerchoice,x)in rules:
            print(f"Oops! You lost. Computer's choice was {computerchoice}")      
    
                  
while True:
     computerchoice=random.choice(choice)
     user_input=input("Enter your choice=").lower()
     if(user_input not in choice):
         print("Invalid input!Enter either snake,water or gun and try again.")
         continue

     yourchoice(user_input)
     
     while True:
          
          ask=input("\nDo you  want to play again?(Yes/No):").lower()
          if ask=="no":
           print("Thanks for playing!")
           exit()
          elif ask=="yes":
            break   
          else:
            print("Enter only either yes or no!\n")
            
     