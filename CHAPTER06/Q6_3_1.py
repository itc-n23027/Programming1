class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "シャリ"
    price = "100"

    def show_attributes(self):
        print(
            "top: {}, base: {}, category: {}, price: {}".format(
                self.top, self.base, self.category, self.price
            )
        )


class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とネギ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
print(k1.show_attributes())
