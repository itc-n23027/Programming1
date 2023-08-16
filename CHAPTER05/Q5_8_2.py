data = [
    ["01", "001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["01", "002", "Male", "Satou", "Takeshi", 25, "Tokyo"],
    ["01", "003", "Female", "Tanaka", "Yuko", 25, "Tokyo"],
    ["02", "001", "Male", "Smith", "Mike", 25, "Tokyo"],
    ["02", "002", "Male", "Turner", "Tom", 25, "Tokyo"],
    ["02", "003", "Male", "Jackson", "David", 25, "Tokyo"],
]

member_information = {}

for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info

print("numbeer", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
