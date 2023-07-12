a = 10
if a > 10:
    a /= 2
else:
    a += 1
print(a)  # 教科書

a = 10
print(a / 2) if a > 10 else print(a + 1)  # 短くしてみた
