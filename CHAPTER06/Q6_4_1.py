import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "See you later",
    "How are you",
    "Have a good day",
    "Good night",
]
with open("some.txt", "w") as f:
    for i in range(10):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

f = open("some.txt")
c = 0
for i in f:
    print(i, end="")
    if c == 2:
        break
    c += 1
print(f.close())
