def power(baseNum,pow):
    n=pro=1
    for n in range(pow):
        pro=pro*baseNum
    return pro
print(power(2,5))