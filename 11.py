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
