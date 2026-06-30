from tkinter import *

def msg():
    #print("Hello world")
    lbl.config(text="Hello")
def clear():
    lbl.config(text="")
root=Tk()

root.title("My Calci")
btn=Button(root,command=msg,font=("Comic Sans Ms",15,"bold"),text="Click Me",
           bg="black",fg="white")
btn.pack()

lbl=Label(root,)
lbl.pack()
btn1=Button(root,command=clear,font=("Comic Sans Ms",15,"bold"),text="Clear Screen",
           bg="black",fg="white")
btn1.pack()
root.geometry("200x200+400+200")
root.wm_iconbitmap("calci.ico")
#root.resizable(0,0,)
root.mainloop()