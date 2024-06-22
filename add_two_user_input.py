one = input("please give first number : \n")
two= input("please provide second :")

# which represents first output

sum= float(one) + float(two)

# print("sum of",one, "and",two, "is", sum)

print("first output >> sum of {0} and {1} is {2}" .format(one,two,sum))


# which represent second output

def add_sum1(one,two):
    return int(one)+int(two)

add_sum1 = add_sum1(one,two)

print("second output >> sum of {0} and {1} is {2}".format(one,two,add_sum1))


# Which is using lambda function

add_sum2 = lambda x,y : int(x)+int(y)

add_sum2 =add_sum2(one, two)

print("third output >> sum of {0} and {1} is {2}".format(one,two,add_sum2))


# which is using the recursive function

def add_sum3(a,b):
    if a==b:
        return int(a)
    elif a>b:
        return  int(b)
    elif a<b:
        return int(a)+int(b)
    else:
        return 0 

add_sum3= add_sum3(one,two)

print("fourth output >> sum of {0} and {1} is {2}".format(one,two,add_sum3))
