import random


print(" Welcome to hangman game!")
print()
print("You have only 6 attempts to guess the word!")

list=["programming","python","hello","development","web","editor","program","welcome","intern","teacher","college","computer","hangman","game","banana"]

value=random.choice(list)
guessed=[]

num=int(input("Press 1 to proceed- "))

if(num==1):
    attempts=6
    blanks =["_"] * len(value)

    print("Word  :"," ".join(blanks))
    while attempts>0 and "_" in blanks:
        guess=input("Enter a character:").lower()
        

        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a valid single digit character")
            continue
        if guess in guessed:
             
             attempts=attempts+1
             print("You have already guessed that letter.",end=" ")
        guessed.append(guess)     
             
        if guess in value:

            for i, char in enumerate(value):
                if guess==char:
                    blanks[i]=guess
            print("good guess!"," ".join(blanks)) 
                 
        else:
            attempts=attempts-1
            print("Incorrect guess! You have ",attempts,"attempts left")
            print("Word:"," ".join(blanks))
                    
    if "_" not in blanks:
            print("Congratulations! You have guessed the word !", value)
    else:
            print("Game over! The word was ", value)    


else:
    print("Thank you! You are welcome whenever you want to play")    