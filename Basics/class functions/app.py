from EmpClass import Employee
emp1=Employee("Joo",60,"IS",True,4.5,5000)
emp2=Employee("Ali",20,"SE",False,2.5,1500)
print(emp1.isExcelent())
print(emp2.isExcelent())
emp1.bonus()
emp2.bonus()