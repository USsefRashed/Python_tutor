class Student:
    no_of_students=0
    def __init__(self,name=None,age=0,courses=None):#Ican intialize values here
        self.__name=name                      # to avoid errors of intialization in parameters in line 13&&14 
        self.__age=age                        #in object -->(notCompletedStd)
        self.__courses=courses
        Student.no_of_students+=1
    #Encapsulate attributes
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_courses(self,courses):
        self.__courses=courses
    def get_courses(self):
        return self.__courses
    #any fuction in class is called method and should have self in pramaeter to get access to class attributes
    def printStudent(self):
        print(f"my name is {self.__name} , my age {self.__age} and my courses [{self.__courses}]")
        #NOTE !! Another way to print by using format
        # print("my name is {} , my age {} and my courses [{}]".format(self.name,self.age,self.courses)) 

    #method to check if the student is old
    def is_old(self,num):
        if self.__age>=num:
            print("the student is old")
        else:
            print("student is not old")

#if I create 2 differnt objects but has the same attributes its ok 
#because each of the stored on another place on memory 
std1=Student("Ali",20,["maths","science"])
std2=Student("Ali",20,["maths","science"])
print(id(std1),id(std2))


# notCompletedStd=Student()#empty object
# print(notCompletedStd.__name,notCompletedStd.__age,notCompletedStd.__courses)#display the __init__parameter's value



#I currently added 3 students let's check
print(Student.no_of_students)
std3=Student("Hossam",12,["IT","CS"])
std3.printStudent()
std1.printStudent()

#the use of is_old function
std1.is_old(50)
std1.is_old(10)

#let's explain Encpsulate
#std2.__name="mohammed"
print(std2.get_name())#NOTE the name didn't changed
#print(std2.__name)#NOTE NOTE NOTE here it will print mohammed but as a new variable
#the perfect way to change class attribute & acheive the encapsulation is
std2.set_name("mohammed")
print(std2.get_name())
print(std2.__name)#Error 'Student' object has no attribute '__name' !!