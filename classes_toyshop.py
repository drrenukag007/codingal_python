class   Toyshop:
    def __init__(self,toylist,name):
        self.toylist=toylist
        self.name=name
        self.lenddict={}
    def displaytoy (self):
            print("We have the following toy in shop")
            for i in self.toylist:
                print(i)

    def lendtoy(self,user,toy):
            self.lenddict.update({toy:user})
            print("the toy has update")

    def addtoy(self,toy):
            self.toylist.append(toy)
            print("the toy has add")


    def returntoy(self, toy):
            self.lenddict.pop(toy)

toys=Toyshop(["trains","cars","doll","doctor-set"],"lets upskill")

while True:
    print("welcome to Upskill Toyshop,enter you choice from below")
    print("1-Disply toys")
    print("2-lend a toys")
    print("3-add a toys")
    print("4-return toys")
    print("5-quit")

    userchoice= int(input("select from the list- "))

    if userchoice == 1:
        toys.displaytoy()

    elif userchoice == 2:
        toy=input("which toy you want- ")
        user=input("your name please- ")
        toys.lendtoy(user,toy)

    elif userchoice == 3:
        toy=input("which toy you want to add to shop- ")
        toys.addtoy(toy)

    elif userchoice == 4:
        toy=input("which toy you want return- ")
        toys.returntoy(toy)

    elif userchoice == 5:
      exit()
    
    