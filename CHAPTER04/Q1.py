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


def outer(a, b):
    print("outer function (a, b) = ({}, {})".format(a, b))

    def inner(c, d):
        print("inner function (c, d) = ({}, {})".format(c, d))
        return 5 * 6

    return inner(a, b)


print(outer(4, 7))


def make_circle_area_func(pi=3.14):
    def circle_area(radius):
        return radius * radius * pi

    return circle_area


circle_area_default = make_circle_area_func()
circle_area_precise = make_circle_area_func(pi=3.1415926535)

type(circle_area_default), type(circle_area_precise)

print(circle_area_default(2))
print(circle_area_precise(2))


def show_message(num=0):
    if num == 0:
        flag = "Red"
        print("=== flag:", flag)
        print("Selection is", num, "which may be the default")
        print("====")
    else:
        flag = "Blue"
        print("=== flag:", flag)
        print("Your choise is", num)
        print("====")


show_message(0)
show_message(1)
