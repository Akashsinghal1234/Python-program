'''
Created on Apr 2, 2016

@author: computer
'''
from Tkinter import *

#import Tkinter
import tkMessageBox



root = Tk() #Makes the window
root.wm_title("Basic Calculator") #Makes the title that will appear in the top left
root.config(background = "#00ff00") #sets background color to white

def addition():
    val1=float(Input1.get())    #String to float
    val2=float(Input2.get())
    
    #val3=int(e2.get());     string to int
    result=val1+val2
    tkMessageBox.showinfo( 'Result is ', "Addition "+str(result))
    Input1.delete(0,END)
    Input2.delete(0,END)

def subtract():
    val1=float(Input1.get())    #String to float
    val2=float(Input2.get())
    #val3=int(e2.get());     string to int
    result1=val1-val2
    #result1=val1-val2
    #str(result)    float to string
    
    tkMessageBox.showinfo( 'Result is ', "Subtraction "+str(result1))
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    Input1.delete(0,END)
    Input2.delete(0,END)

def quit():
    root.destroy()


leftFrame = Frame(root, width=500, height = 500)

leftFrame.grid(row=0, column=0, padx=50, pady=2)

Label(leftFrame, text="Basic Calculator").grid(row=0, column=1, padx=10, pady=2)

l1=Label(leftFrame, text="First Number").grid(row=2, column=0, padx=10, pady=2)
Input1 = Entry(leftFrame, width = 20) #the width refers to the number of characters
Input1.grid(row=2, column=1, padx=10, pady=2)

Label(leftFrame, text="Second Number").grid(row=4, column=0, padx=10, pady=2)

Input2 = Entry(leftFrame, width = 20) #the width refers to the number of characters
Input2.grid(row=4, column=1, padx=10, pady=2)



b1=Button(leftFrame, text='Quit', height=1, width=8,command=quit)
b1.grid(row=6, column=0, sticky=W, padx=10, pady=10)

b2=Button(leftFrame, text='ADD', height=1, width=8,command=addition)
b2.grid(row=6, column=1, sticky=W, padx=10, pady=10)
b3=Button(leftFrame, text='subtract', height=1, width=8,command=subtract)
b3.grid(row=6, column=2, sticky=W, padx=10, pady=10)

root.mainloop( )