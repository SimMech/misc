import tkinter
from tkinter import messagebox
from tkinter import *
top=tkinter.Tk()
checkvar1=IntVar()
checkvar2=IntVar()
c1=Checkbutton(top,text='Music', variable=checkvar1,
               onvalue=1, offvalue=0, height=5, width=20)
c2=Checkbutton(top,text='Video', variable=checkvar2,
               onvalue=1, offvalue=0, height=5, width=20)
c1.pack()
c2.pack()
top.mainloop()