# program to reverse the number 


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
