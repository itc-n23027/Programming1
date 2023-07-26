def my_func(x):
    x.append(1)


my_list = [0, 1, 2, 3]
my_func(my_list)

print(my_list)


def my_func(x):
    result = [0]
    return result * x


print(my_func(3))


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


print(fib(15))

i_num_list = range(1, 11)
s_num_list = list(map(lambda i: str(i) + "番", i_num_list))
print("文字列リスト:", s_num_list)

for e in filter(lambda i: i % 2 == 0, range(1, 11)):
    print(e, end="")

pairs = [(2, "down"), (1, "up"), (4, "charm"), (3, "strange")]
pairs.sort(key=lambda x: x[0])
print(pairs)
