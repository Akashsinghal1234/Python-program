# Ask for enter the number from the use  

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



