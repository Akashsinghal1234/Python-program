import random
while True:
    st=input("enter the word for password generate ")
    pwd=""
    print("1 for generate password\n2 for not generate password")
    num=int(input ("enter the choice "))
    if num == 1:
              for i in range (len(st)):
                r1=random.randint(0, 5)
                x=ord(st[i])
                y=x+r1
                z=y-1
                pwd=pwd+chr(y)+chr(z)
              print(pwd)
    else:
            print(st)

    val=input("do you want to conti press y else n ")
    if val!='y':
            break
