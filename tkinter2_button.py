from tkinter import *

def msg():
    print("Hello world")
def add():
    print(9+12)
root=Tk()

root.title("My Calci")
btn=Button(root,command=msg,font=("Comic Sans Ms",15,"bold"),text="Click Me",
           bg="black",fg="white")
btn.pack()


btn1=Button(root,command=add,font=("Comic Sans Ms",15,"bold"),text="Show ",
           bg="black",fg="white")
btn1.pack()
root.geometry("200x200+400+200")
root.wm_iconbitmap("calci.ico")
#root.resizable(0,0,)
root.mainloop()