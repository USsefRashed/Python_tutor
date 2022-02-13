from datetime import date
class Student:
    def __init__(self,name=None,age=0):
       #class attributes                            
        self.__name=name
        self.__age=age
    def printStudent(self):
        print(f"my name is {self.__name} , my age {self.__age} ")
        #NOTE !! Another way to print by using format
        # print("my name is {} , my age {} and my courses [{}]".format(self.name,self.age,self.courses)) 
#   '@' this is decorator by which I tell the method how to work with specific way with out modify or chang it
    @classmethod                #take a class as a parameter so it cannot modify class attributes
    def initFromBirthYear(cls,name,birthYear):#cls=class
        return cls(name,date.today().year-birthYear)
std1=Student("yousef",19)
std2=Student.initFromBirthYear("ahmed",1993)
std2.printStudent()
std1.printStudent()


#let's create pizza class
class Pizza:
    def __init__(self,ingredients):
        self.components=ingredients
    @classmethod
    def veg(cls):
        return cls(['Mashroum','olives','onions'])
    @classmethod
    def margerita(cls):
        return cls(['mozirilla','saude'])
    def __str__(self):
        return f"pizza ingraedients is {self.components}"
pz1=Pizza(['tomatoes','olives'])
pz2=Pizza.veg()
pz3=Pizza.margerita()
print(pz2)