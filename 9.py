
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
