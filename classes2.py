class Expression:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def addition(self):
        result = self.num1 + self.num2 + self.num3
        print(result)

calculation = Expression(5,7,10)
calculation.addition()

calculation_1 = Expression(10,22,40)
calculation_1.addition()


calculation_2 = Expression(15,32,402)
calculation_2.addition()
