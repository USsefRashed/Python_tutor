class Employee:
    def __init__(self,name,age,dep,is_manager,rating,salary):
        self.name=name
        self.age=age
        self.dep=dep
        self.is_manager=is_manager
        self.rating=rating
        self.salary=salary
    def isExcelent(self):
        if self.rating>2.5:
            return True
        else:
            return False
    def bonus(self):
        if self.age==60:
            self.salary+=1000
            print("slary increased by 1000 = " ,str(self.salary))
        else:
            print("No bonnus UR salary Still "+str(self.salary))

 

        