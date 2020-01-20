from tkinter import *
root=Tk()
# lab=Label(root,text="Quresh")

f1=Frame(root)
bt1=Button(f1,text="H1",bg="red")
bt1.pack(side=TOP)

bt2=Button(f1,text="H2",bg="green")
bt2.pack(side=LEFT)

bt3=Button(f1,text="H3",bg="blue")
bt3.pack(side=BOTTOM)


f1.pack()


f2=Frame(root)
bt4=Button(f2,text="H4",bg="yellow")
bt4.pack()

f2.pack(side=BOTTOM)

# lab.pack()
root.mainloop() 	