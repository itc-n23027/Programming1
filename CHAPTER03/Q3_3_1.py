my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
print(my_list_6)  # 教科書

my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
print([i for i in my_list if len(i) >= 6])  # 短くした
