def add(x,y):
    return x+y

def devision(x,y):
    if y==0:
        return "Maths Error !"
    return x/y

def subtract(x,y):
    return x-y

def product(x,y):
    return x*y

def power(baseNum,pow):
    n=pro=1
    for n in range(pow):
        pro=pro*baseNum
    return pro



print("\tWelcome to my calculator\n")
num1=float(input("Enter the first number : "))
oper=input("Enter operation (/ + ^ - *)")
num2=float(input("Enter the second number : "))
if oper=="+":
    print(num1," + ",num2," = ",add(num1,num2))
elif oper=="*":
    print(num1," * ",num2," = ",product(num1,num2))
elif oper=="-":
    print(num1," - ",num2," = ",subtract(num1,num2))
elif oper=="/":
    print(num1," / ",num2," = ",devision(num1,num2))
elif oper=="^":
    print(num1," ^ ",num2," = ",power(num1,int(num2)))
else:
    print("You should choose from (/ + * - ^)")