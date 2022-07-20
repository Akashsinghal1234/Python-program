#Factors of a Positive Integer

num=int(input("Enter a positive integer: "))
i=1
while i<=num:
         if num % i == 0:
                  print(i)
         i=i+1
