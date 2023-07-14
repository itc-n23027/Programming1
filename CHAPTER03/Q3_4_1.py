for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 教科書

print("\n".join([str(i) for i in range(10) if i % 2 != 0]))
print(*[i for i in range(10) if i % 2 != 0], sep="\n")  # 短くした
