b = ""
a = 23
while a != 0:
    a, r = divmod(a, 2)
    b = str(r) + b
print(b)
