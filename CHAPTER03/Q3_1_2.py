a = 0
if a == 0:
    a += 1
    a *= 2
    a -= 1
print(a)  # 教科書

a = 0
print((a + 1) * 2 - 1) if a == 0 else print("error")  # 短くした
