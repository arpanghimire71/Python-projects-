import time

localtime=int(time.strftime("%H"))


if(localtime>=1 and localtime<12):
    print("Goodmorning user!")
elif(localtime>=12 and localtime<18): 
    print("Good afternooon user!")  
else:
    print("Good evening user")     

