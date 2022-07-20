#program to check whether a number is palindrome or not 

# Ask for enter the number from the use  
number = int(input("Enter the integer number: "))  

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

