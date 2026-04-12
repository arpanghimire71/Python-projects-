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
print(data)
words=data.split()
words=len(words)
print(words)
print(len(data))
char=0
for i in data:
    if i.isalpha():
        char=char+1
print(char)        