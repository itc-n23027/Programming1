my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in my_list:
    if n % 2 != 0:
        x += n
print(x)  # 教科書

my_list = [1, 1, 2, 3, 5, 8, 13]
x = sum([i for i in my_list if i % 2 != 0])
print(x)  # 短くした
