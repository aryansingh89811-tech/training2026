from tkinter import *

def msg():
    print("Hello world")
def add():
    print(9+12)
root=Tk()

root.title("My Calci")
btn=Button(root,command=msg,font=("Comic Sans Ms",15,"bold"),text="Click Me",
           bg="black",fg="white")
btn.pack(side="top")


btn1=Button(root,command=add,font=("Comic Sans Ms",15,"bold"),text="Show1 ",
           bg="blue",fg="white")
btn1.pack(side="right")

btn2=Button(root,command=add,font=("Comic Sans Ms",15,"bold"),text="Show2 ",
           bg="red",fg="white")
btn2.pack(side="left",fill="y")

btn3=Button(root,command=add,font=("Comic Sans Ms",15,"bold"),text="Show3 ",
           bg="green",fg="white")
btn3.pack(side="bottom",fill="x")
root.geometry("400x400+400+200")
root.wm_iconbitmap("calci.ico")
#root.resizable(0,0,)
root.mainloop()