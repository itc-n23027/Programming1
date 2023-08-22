class myclass1:
    def __init__(self, text="abc"):
        self.text = text


a = myclass1()
b = myclass1(text="ggg")
c = myclass1(text="uds")

print(a.text)
print(b.text)
print(c.text)


class myclass2:
    common_text = "class value"


print(myclass2.common_text)
myclass2.common_text
common_text = "newclass value"
print(myclass2.common_text)
