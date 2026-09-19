import random
import time

data=[
    "A quick brown fox jumps over a  lazy white dog",
    "Bright stars twinkle silently in the midnight sky",
    "Coding challenges sharpen your logic and patience",
    "A rolling stone gathers no moss",
    "She sells seashells by the seashore",
    "Knowledge is power but wishdom is peace",
    "The rain in Spain falls mainly on the plain ",
    "Every great journey begins with a small step",
    "Practice makes perfect, but consistency makes progress",
    "Time waits for no one, so type faster today "
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
your_type=input("Enter your typed text:")
for i,j in zip(data,your_type):
    if i!=j:
        error=error+1
correct_text=len(data)-error
        