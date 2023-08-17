def square(x):
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.sidigit():
            x = int(x)

        else:
            raise ValueError("square", x)
    return x**x


print(square(2))
print(square("a"))
