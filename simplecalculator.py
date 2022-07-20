import getpass
import sys
xpass = getpass.getpass('Enter The Password For Run The Application ')

if xpass == "akash":
    def xsum(x,y):
        print("sum of two number is ",x+y)

    def xsub(x,y):
        print("subtraction of two number is ",x-y)

    def xmul(x,y):
        print("mul of two number is ",x*y)

    def xper(x,y):
        result = n1*(n2/100)
        print("Percentage of Number Is ",result)

    def sq(x):
        result = x*x
        print("sq of Number Is ",result)

    def fact(x):
        i=x
        result=1
        while (i > 0):
            result = result*i
            i=i-1
        print("factorical of number is " ,result)

    def xdivide(x,y):
        print("mul of two number is ",x/y)

    def cube(x):
        result = x*x*x
        print("cube of Number Is ",result)


    while True:
        print("1. For Addition\n2. for Subtraction\n3. for multipication\n4. for percentage\n5. for square \n6. for Factorical \n7. for divide \n8. for cube\n9. for Exit")
        num=int(input("Enter your choice "))
        if(num == 1):
            n1 = int(input("Enter the first Number "))
            n2 = int(input("Enter the Second Number "))
            xsum(n1,n2)
        if(num == 2):
            n1 = int(input("Enter the first Number "))
            n2 = int(input("Enter the second Number "))
            xsub(n1,n2)
        if(num == 3):
            n1 = int(input("Enter the first Number "))
            n2 = int(input("Enter the second Number "))
            xmul(n1,n2)
        if(num == 4):
            n1 = int(input("Enter The Number "))
            n2 = int(input("Enter The Percentage "))
            xper(n1,n2)
        if(num == 5):
            n1 = int(input("Enter The Number for Squere "))
            sq(n1)
        if(num == 6):
            n1 = int(input("Enter The Number for factorical "))
            fact(n1)
        if(num == 7):
            n1 = int(input("Enter the first Number "))
            n2 = int(input("Enter the second Number "))
            xdivide(n1,n2)
        if(num == 8):
            n1 = int(input("Enter The Number for cube "))
            cube(n1)
        if(num == 9):
            sys.exit()
            

        ans = input("Do you Want To Contionue press y else n ")
        if ans != 'y':
            break

else:
    print("incorrect password")
