from tkinter import *

def printHello():
    print("Hi!!!!!!!")


root=Tk()


l1=Label(root, text="Python Test")
b1=Button(root, text="Hello Python", command=printHello)
c=Button(root, text="Quit", command=root.quit)


l1.pack()
b1.pack()
c.pack()

root.mainloop()
