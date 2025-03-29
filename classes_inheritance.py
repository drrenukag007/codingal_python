class Boss():
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def disply(self):
        print(self.name)
        print(self.id)

class Employee(Boss):
    def __init__(self,name,id,salary,designation):
        Boss.__init__(self,name,id)
        self.salary=salary
        self.designation=designation
Ram=Employee("Ram",100,100000,"VP")
Ram.disply()

sam=Employee("Sam",200,500000,"SVP")
sam.disply()
