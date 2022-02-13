# #General exception
# try:
#     result=10/0
# except :
#     print("invalid value")
#print("Sccess")

# #specific exception
# try:
#     result=10/0
# except ZeroDivisionError as err1:
#     print(err1)
#print("Sccess")

#2 Exceptions in the same code 
# try:
#     value=int(input("Enter integer not str"))
#     print(value)
#     result=10/0
# #NOTE !! the specify excption like 0 exception should come 
# # first before the general exception 
# except ZeroDivisionError as err1:
#     print(err1)
# except :
#     print("invalid input")

# print("Sccess")

#ALIASES rename exception
try:
    value=int(input("Enter integer not str"))
    print(value)
    result=10/0
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2 :
    print(err2)#run to see what will print

print("Sccess")