import random


class guessnum():
    def __init__(self):
        self.num=random.randint(1,100)

    def play(self):
        print("Welcome to the number guessing game-")
        attempts=0
        
        
        while True:
            try:
                yourguess=int(input("Enter your guess between 1 and 100-"))
                if(yourguess<1 or yourguess>100):
                    print("Error! Enter the value in range 1-100") 

                elif(yourguess>self.num):
                    print("Go little lower")
                    attempts=attempts+1  
                elif(yourguess<self.num):
                    print("Go little higher!")  
                    attempts=attempts+1  
                elif(yourguess==self.num):
                    print("Your guess is correct! in ",attempts,"attempts")
                    break 
                else:
                    print()
            except ValueError:
                print("Error! Enter valid number between and 100")          
                 
obj=guessnum() 
obj.play()            
