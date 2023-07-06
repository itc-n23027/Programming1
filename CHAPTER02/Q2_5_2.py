answer = ""
w = "○ "
b = "● "
for i in range(10):
    for j in range(10):
        if i == j:
            answer += w
        else:
            answer += b
    answer += "\n"
print(answer)
