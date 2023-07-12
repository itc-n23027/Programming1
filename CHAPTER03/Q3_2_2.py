a = 100
if a >= 100:
    a *= 2
elif 50 <= a < 100:
    a /= 2
else:
    a += 2
print(a)  # 教科書

a = 100
print(a * 2) if a >= 100 else print(a / 2) if a <= a < 100 else print(a + 2)
# 短くしてみた
