#WAP program to swap two number which enter by user using third variable

n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))


print("value before swap",n1,n2)

temp = n1
n1 =n2
n2=temp

print("values after swap",n1,n2)
