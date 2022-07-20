#check whether a number is prime or not


switch=0

number = int(input("enter the number ")) 

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
         
