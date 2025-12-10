timeformat=int(input("Enter the time format used in your region-24hr/12 hr ="))

if(timeformat==24):
    hour,min=map(int,input("Enter your time in hr min format=").split())

    try:
        if(hour>=1 and hour<12):
            print("Good morning  user!")
        elif(hour>=12 and hour<18):
            print("Good afternoon user!") 
        else:
            print("Good evening user!")    
    except ValueError:
            print(" Value error! Please enter the correct time in provided format ")
            

if(timeformat==12):
    hour,min=map(int,input("Enter your time in hr,min format=").split())
    shift=input("Enter the shift-AM/PM= ")

    if(shift.upper()!="AM" and shift.upper()!="PM"):
        print("Enter your shift properly!")
    else:
        try:
            if(shift.upper()=="AM"):
                print("Good morning user!")
            
            
            if(shift.upper()=="PM"):
                if(hour>=1 and hour<6):
                    print("Good afternoon user!")
                
                if(hour>5 and hour<13):
                    print("Good evening user!")
                
                
        except ValueError:
            print(" Value error! Please enter the correct time in provided format ")   
            
         

    

    

                        
           
         