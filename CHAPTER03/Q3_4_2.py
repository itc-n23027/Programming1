numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n
print(x)  # 教科書

print(sum([i for i in numbers if i < 10]))  # 短くした
