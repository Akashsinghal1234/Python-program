#A leap year is exactly divisible by 4
#except for century years (years ending with 00).
#century year is a leap year only if it is perfectly divisible by 400.


#For example,

#1999 is not a leap year
#2000 is a leap year
#2004 is a leap year





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

