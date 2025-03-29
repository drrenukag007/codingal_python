class Money:
    def __init__(self):
        self.__price=10000

    def sell(self):
        print(self.__price)

    def changeprice(self,price):
        self.price=price

mone=Money()
mone.sell()
mone.changeprice(20000)
mone.sell()


class Square:
    def __init__(self):
        self.__side=20

    def area(self):
        print("the side is ",self.__side)
        print("the area of square ",self.__side*self.__side)

sq=Square()
sq.__side=30
sq.area()
