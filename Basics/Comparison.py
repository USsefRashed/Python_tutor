# def maxNum(num1,num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
# print("The max number is ",maxNum(5,10,900))
def maxString(str1,str2,str3):
    if str1>=str2 and str1>=str3:
        return str1
    elif str2>=str1 and str2>=str3:
        return str2
    else:
        return str3
print("Max string is : ",maxString("Ali","Joo","Yousef"))