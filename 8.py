'''1
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
