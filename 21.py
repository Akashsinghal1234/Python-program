'''
---*
--**
-***
****
'''


# 4 is rows    space 4
# 4 is space
space = 3 #row-1
i = 1
while i<=4:
         p=1
         while p<=space:  
                  print("-",end="")
                  p=p+1
         q=1
         while q<=i:
                  print("* ",end="")
                  q=q+1
         print()
         space = space -1
         i=i+1
