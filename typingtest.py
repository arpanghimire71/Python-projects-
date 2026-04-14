
import random
import time
import keyboard

data=[
    "A quick brown fox jumps over a lazy white dog",
    "Bright stars twinkle silently in the midnight sky",
    "Coding challenges sharpen your logic and patience",
    "A rolling stone gathers no moss",
    "She sells seashells by the seashore",
    "Knowledge is power but wisdom is peace",
    "The rain in Spain falls mainly on the plain",
    "Every great journey begins with a small step",
    "Practice makes perfect, but consistency makes progress",
    "Time waits for no one, so type faster today"
]
data=random.choice(data)
words=data.split()
words=len(words)


char=0
for i in data:
    if i.isalpha():
        char=char+1
error=0
print("Total characters in this sentences:",char)
print("Total words in this sentence:",words)
print("TYPE:",data)

start_time=None
while True:
    event=keyboard.read_event()
    if event.event_type==keyboard.KEY_DOWN:
        if start_time==None:
            start_time=time.time()

your_type=input("Enter your typed text:")
end_time=time.time()
elapsed_time=(end_time-start_time)/60

for i,j in zip(data,your_type):
    if i!=j:
        error=error+1
if(your_type.strip()==""):
    print("No any typed text:")
else:
    correct_text=len(data)-error
    accuracy=(correct_text/len(data))*100
    wpm=int((len(your_type)/5)/elapsed_time)
    print("Your typing speed is ",wpm,"wpm with accuracy ",accuracy,"%")               