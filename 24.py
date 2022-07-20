
'''
---*
--**
-***
****
****
-***
--**
---*
'''

#------------first part -------------
i = 1
space = 4
while i<=4:
         p=1
         while p<space:
                  print("-",end="")
                  p=p+1
         q=1
         while q<=i:
                  print("* ",end="")
                  q=q+1
         print()
         i=i+1
         space = space -1

#-----------------second part----------
i = 4
space = 1
while i>=1:
         p=1
         while p<space:
                  print("-",end="")
                  p=p+1
         q=1
         while q<=i:
                  print("* ",end="")
                  q=q+1
         print()
         i=i-1
         space = space +1

'''

'''
#ASCII value to characters chr(number)


i=1 #row
num = 65
while i <=4:
         j=1 #column
         while j<=i:
                  print(chr(num),end="")
                  j=j+1
                  num=num+1
         print()
         i=i+1
         #num = num+1
'''



'''
i=1
while i<=10:
         print(i)
         i = i+1
'''


#range(10)   0123456789
'''
for i in range(10):
         print(i)
'''
'''
for i in range(4):
         for j in range(4):
                  print( i, j, i+j)

'''

'''
for i in range(10,2,-1):
         print(i)

'''

'''
for i in range(-50 ,100 , 50):
         print(i) 
'''
'''
#1 2 4 6 8 9
for i in range( 1,10,2): #20 17 14 11
         print(i)








