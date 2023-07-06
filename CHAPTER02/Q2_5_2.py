answer = ""
w = "○ "
b = "● "
for i in range(4):
    for j in range(4):
        if i == j:
            answer += w
        else:
            answer += b
    answer += "\n"
print(answer)
