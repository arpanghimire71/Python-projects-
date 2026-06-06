# encoding decoding program 

# write a python program to translate a message into a secret code lasnguage.
# coding:
# if the word contains at least three characters,remove the first letter and append it to the end
# and now append three random characters at the starting and the End

# else:
# simply reverse the string


# decoding:
# if the word contains less than 3 characters ,then simply reverse the string
# else:
#     remove three random characters from start and end .Now remove the last letter and add it to the beginning.
#program should ask whether you want to code or decode

import random
symbol=["a","b","c","d","e","f","g","h","i"
      ,"j","k","l","m","n","o","p","q","r",
      "s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9",
      "10","!","@","#","$","%","^","^","&","*","(",")"]

word=input("Enter a word=")

def arrange(word):
    newword1=word[1:]+word[0]
    ch1=''.join(random.sample(symbol,3))
    ch2=''.join(random.sample(symbol,3))
    newword=ch1+newword1+ch2
    return newword

def dearrange(word):
    coreword=word[3:-3]
    decoded_word=coreword[-1]+coreword[0:-1]
    return decoded_word

def code(yourneed):
    encode=""
    decode=""
    try:
        if(yourneed=="1"):
            if len(word)<3:
                length=len(word)
                for i in range(len(word)):
                    encode=encode+word[length-1]
                    length=length-1
                print("Encoded word=",encode) 

            elif len(word)>=3:
                print("Encoded word=",arrange(word))   

        elif(yourneed=="2"):
            if len(word)<3:
                length2=len(word)
                for i in range(len(word)):
                    decode=decode+word[length2-1]
                    length2=length2-1
                print("Decoded word=",decode)

            elif len(word)>=3:
                print("Decoded word=",dearrange(word))

        else:
            raise ValueError("Invalid choice ")        

    except :
        print("Only enter either 1 or 2")

yourneed=input("Press 1 to encode the message or 2 to decode the message= ") 
code(yourneed)     