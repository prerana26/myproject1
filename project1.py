from user_pass import *
from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("Blood Bank")
lab1=Label(root,text="Login",width=30,font=("bold",20))
lab2=Label(root,text=" username :-").place(x=60,y=80)
e1=Entry(root).place(x=140,y=80)
lab3=Label(root,text="password:-").place(x=60,y=120)
e2=Entry(root).place(x=140,y=120)
bt=Button(root,text="SUBMIT",command=username).place(x=120,y=160)
lab1.pack()











root.mainloop()
