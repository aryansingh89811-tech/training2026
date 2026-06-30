from tkinter import *
root=Tk()
def getValue():
    data=a.get()
    print(data)
    a.set(0)
root.title("My Calci")
lbl=Label(root,text="Enter first number",
          font=("Comic Sans Ms", 15, "bold"),
          bg="black", fg="white"
          )
lbl.place(x=50,y=50)
a=IntVar()
input1=Entry(root,textvariable=a,font=("Comic Sans Ms", 15, "bold"),
          bg="black", fg="white")
input1.place(x=300,y=50)

btn=Button(root,font=("Comic Sans Ms",15,"bold"),text="Show2 ",
           bg="red",fg="white",command=getValue)
btn.place(x=200,y=100)
root.geometry("600x400+100+100")
root.wm_iconbitmap("calci.ico")
root.mainloop()
