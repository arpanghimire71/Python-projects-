# KBC game
print("Welcome to the KBC game")
print("The amount you will be awarded for the correct answers of respective qn no. is listed below: ")
prize={
    "For Question no":"Prize",
    "1": "Rs.1000",
    "2": "Rs.2000",
    "3": "Rs.4000"
}
for key,value in prize.items():
    print(key,":",value)


amount=0   
questions=["What is the capital city of Nepal?","Who is the current PM of nepal?","2+2=??"]


for i in range(len(questions)):
    print("qn no.",i+1)
    print(questions[i])
    if(i==0):
        
        print("a.Biratnagar",end='  ')
        print("b.Kathmandu",end='\n')
        print("c.Birgunj",end=' ')
        print("d.POkhara",end='\n')
        yourans=input("Your answer is option no ??a/b/c/d:")
        yourans=yourans.lower()
        
        if(yourans=='b'):
            print("Your answer is correct:")
            amount=amount+1000
        else:
            print("Oops!Your answer is wrong: You lost the game.Better luck next time:") 
            break;  
    elif(i==1):
        print("a.KP oli",end='  ')
        print("b.Sherbahadur Deuba",end='\n')
        print("c.Puspakamal Dahal",end=' ')
        print("d.Sushila Karki",end='\n')
        yourans=input("Your answer is option no ??a/b/c/d:")
        yourans=yourans.lower()
        
        if(yourans=='d'):
            print("Your answer is correct:")
            amount=amount+2000;
        else:
            print("Oops!Your answer is wrong: You lost the game.Better luck next time:") 
            break;   
    elif(i==2):
        print("a.4",end='  ')
        print("b.6",end='\n')
        print("c.9",end=' ')
        print("d.5",end='\n')
        yourans=input("Your answer is option no ??a/b/c/d:")
        yourans=yourans.lower()
        
        if(yourans=='a'):
            print("Your answer is correct:")
            amount=amount+4000;
        else:
            print("Oops!Your answer is wrong: You lost the game.Better luck next time:") 
            break;   
     
print("You have won rs.",amount);
print("Thank you")     


