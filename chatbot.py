import sys

print("Hey there! How can I help you today?")

def reply(question):
        if "hello" in question:
         print("Hi ! This is an automated chatbot . How can I help \n you today. You can type \" bye \" if you want to exit! ")
         
         
        elif "how are you?" in question:
         print(" I am fine .Thank you !")
         return True
        elif "bye" in question:
         print("Goodbye! See you soon....")  
         sys.exit()
        
        else:
         print("I am extremely sorry that I am unable to respond to your request ")  
         return True
    
      

while True:
  ask=input().lower()
  reply(ask)

        
  