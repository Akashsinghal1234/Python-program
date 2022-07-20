#WAP to multiple three number and get the input from user
'''
n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
n3 = int(input("enter the thrid number"))
result = n1*n2*n3
print("result after multiple three is",result);
'''


#WAP to four number from user and display the sum of it.
#WAP to display the squaru of the number and take the number from user.
#WAP to find area of the circle and insert rideus from user.
#3.14*r*r

#WAP program to swap two number which enter by user using third variable
'''
n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))


print("value before swap",n1,n2)

temp = n1
n1 =n2
n2=temp

print("values after swap",n1,n2)
'''

#WAP program to swap two number which enter by user without using
#third varible


#find the intrest from progam principle and rate and time enter by user


#print the qube of the number and number enter by the user.


#find the netprice after discount on the product price.
'''
take product price from user
take discount rate from user

netprice = price - (price*discountrate/100)


1000
10%

netprice  1000 - 1000*10/100 = 900
'''



#wap to get minutes from user
#and print hour and left minutes

#division
#floor division

'''
n1 =10

n2 = 3

div = n1//n2

print(div)
'''











































'''
#/division vs // floor division

#/ is division
#// Floor division ( means after performing the division, results 		            in the lower integer to the value.)

print(10/3)                # mathematical result is 3.33333333333

print(10//3)                 #3.0 < 3.333333 < 4.0
'''


# program to reverse the number


    
'''
x = 3456

lastnumber = x%10

remaingnumber = x//10
print(lastnumber)
print(remaingnumber)
'''





# Ask for enter the number from the use  
'''
number = int(input("Enter the integer number: "))  
# Initiate value to null   4675
revs_number = 0                      
# reverse the integer number using the while loop  
i = number  
while (i > 0):  
    # Logic  
    lastnumber = i % 10   
    revs_number = (revs_number * 10) + lastnumber
    i = i // 10 
  
# Display the result  
print("The reverse number is ",revs_number)
if number == revs_number:
         print("number is palindrome")
else:
          print("number is not palindrome")
'''







# program to reverse the number 

'''
# Ask for enter the number from the use  
number = int(input("Enter the integer number: "))  
  
# Initiate value to null   4675
mul = 1                    
  
# reverse the integer number using the while loop  
  
while (number > 0):  
    # Logic  
    remainder = number % 10   
    mul = mul* remainder   
    number = number // 10 
  
# Display the result  
print("The product of  number is ",mul)
'''
'''
1
12
123
1234
A
AB
ABC
ABCD

*
**
***
****
'''

'''
for i in range(1,5):
         print("A"*i)
'''
'''

for i in range(1,5):
         X=65
         for j in range(1,i+1):
                  print(chr(X),end="")
                  X=X+1
         print("")
'''
'''
X= 'A'

print(ord(X))
'''


         


'''
Explanation -

Let's understand this program step by step.

We initialed a number variable for user input and variable revs_number initial value to null.

First Iteration

Reminder = number %10
Reminder = 12345%10 = 5
Reverse = Reverse *10 + Reminder Initial value of revs_number is null
Reverse = 0 * 10 + 5 = 0 + 5 = 5
Number = Number //10
Number = 1234 //10 = 1234 // Now loop will iterate on this number.
Second Iteration

Now the number is 123, and the revs_number is 5. The while checks its condition and executes for the next iteration.

Reminder = Number % 10
Reminder = 1234 % 10 = 4
Reverse = Reverse *10+ Reminder = 5 * 10 + 4
Reverse = 50 + 4 = 54
Number = Number //10 = 12345 //10
Number = 123
Third Iteration

From the Second Iteration, the values of both Number and Reverse have been changed as: number = 123 and revs_number = 54

Reminder = Number %10
Reminder = 123%10 = 3
Reverse = Reverse *10+ Reminder = 54 * 10 + 3
Reverse = 540 + 3 = 543
Number = Number //10 = 123//10
Number = 12
Fourth Iteration

The modified number is 12 and the revs_number is 543: Now while executes again.

Reminder = Number %10
Reminder = 12 %10 = 2
Reverse = Reverse *10+ Reminder = 543 * 10 + 2
Reverse = 5430 + 2 = 5432
Number = Number //10 = 12//10
Number = 1
Fifth Iteration

Reminder = Number %10
Reminder = 1 %1 0 = 1
Reverse = Reverse *10+ Reminder = 5432 * 10 + 1
Reverse = 54320 + 1 = 54321

'''


'''
#check Armstrong number ex is 153,370,371,407
#1*1*1 + 5*5*5 + 3*3*3  =  153

num = int(input("Enter a number: "))  
sum = 0  
i = num  

#sum =3**3 + 4**3 + 1**3
  
while i > 0:  
   digit = i % 10   
   sum = sum + digit ** 3  
   i = i // 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
'''
'''
#program to check whether a number is palindrome or not 

# Ask for enter the number from the use  
number = int(input("Enter the integer number: "))  12321

numbercheck = number
# Initiate value to null  
revs_number = 0  
  
# reverse the integer number using the while loop  
  
while (number > 0):  
    # Logic  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
   

if revs_number == numbercheck :
         print("is a palindrome.")
else:
         print("is not a palindrome.")
'''


#12321
#12321

'''
#Python Program to Print the Fibonacci sequence

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on....  

    nterms = int(input("How many terms you want? ")) #4
# first two terms  
n1 = 0
n2 = 1  
i = 3  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while i <= nterms:
       next = n1 + n2  
       print(next,end=' , ')  
       # update values  
       n1 = n2  
       n2 = next  
       i = i + 1
'''


'''

#Program to Check if a Number is Odd or Even

num = int(input("Enter a number: "))
i = 1
while i <= 100:
         if (i % 2) == 0:  
            print("Even number",i)  
         else:  
            print("Odd number",i)
         i=i+1


'''



#check whether a number is prime or not

'''
switch=0

number = int(input("enter the number ")) 21

i=2
while i < number:
         if number%i==0:
                  switch=1
                  break
         else:
                  switch = 0
         i=i+1

if switch == 1:
         print("number not is prime")
else:
         print("number is prime")
         
'''










#A leap year is exactly divisible by 4
#except for century years (years ending with 00).
#century year is a leap year only if it is perfectly divisible by 400.


#For example,

#1999 is not a leap year
#2000 is a leap year
#2004 is a leap year




'''
year = int(input("Enter a year: "))

#leap year if perfectly visible by 400
if year % 400 == 0:
         print("leap year ", year);
elif year % 100 == 0: #not a leap year if visible by 100 but not divisible by 400
         print(" is not a leap year.", year)
elif year % 4 == 0: #leap year if not divisible by 100 but divisible by 4
         print(" is a leap year.", year)
else: #all other years are not leap year
         print("%d is not a leap year.", year)


'''
'''
#Find the Sum of Natural Numbers
#N= {0, 1, 2, 3, 4, .... and so on}

num = int(input("Enter a number: ")) 10 
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum = sum + num  
       num = num - 1  
   print("The sum is",sum)  
'''

'''
#Python program to generate a random number

import random  
print(random.randint(1,3))  # randint(start,end-1) 
''

#Python program to convert Celsius to Fahrenheit

#c =(f-32)*5/9   fahrenheit to celsius
#f =(c*9/5)+32   celsius to fahrenheit


#Python program to convert Celsius to Fahrenheit
'''
# Collect input from the user  
#celsius = float(input('Enter temperature in Celsius: '))  
  
# calculate temperature in Fahrenheit  
#fahrenheit = celsius * (9/5) + 32  
#print('Celsius is equal to degree Fahrenheit',celsius,fahrenheit)  
'''

#Python Program to swap two numbers without using third variable

'''
'''
# Python code to swap two numbers 
# without using another variable 
  
'''  
x = 5
y = 7
  
print ("Before swapping: ") 
print("Value of x : ", x, " and y : ", y) 
  
# code to swap 'x' and 'y' 
x, y = y, x 
  
print ("After swapping: ") 
print("Value of x : ", x, " and y : ", y) 

'''
'''
'''
#Factors of a Positive Integer

num=int(input("Enter a positive integer: "))
i=1
while i<=num:
         if num % i == 0:
                  print(i)
         i=i+1
'''
'''
'''
'''
*
**
***
****

****
***
**
*


1
12
123
1234


1
23
456
78910

A
BC



 *
***
'''

'''



