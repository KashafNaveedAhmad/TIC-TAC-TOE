import tkinter as tk
from tkinter import *
from tkinter import messagebox

def button_click(Button):
    global x_o,flag
    Button["bg"]="#808080"
    if Button["text"]=="" and x_o==True:
        Button["text"]="X"
        x_o=False
        flag=flag+1
    elif Button["text"]=="" and x_o==False:
        Button["text"]="O"
        x_o=True
        flag=flag+1    
    else:
        messagebox.showinfo("Player entered!")   
        
    
main=Tk()
main.title("TIC TAC TOE") 

x_o=True
flag=0

Button1=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button1))
Button1.grid(row=0,column=0)
Button2=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button2))
Button2.grid(row=0,column=1)
Button3=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button3))
Button3.grid(row=0,column=2)
Button4=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button4))
Button4.grid(row=1,column=0)
Button5=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button5))
Button5.grid(row=1,column=1)
Button6=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button6))
Button6.grid(row=1,column=2)
Button7=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button7))
Button7.grid(row=3,column=0)
Button8=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button8))
Button8.grid(row=3,column=1)
Button9=Button(main,text="",font=("arial",45,"bold"),bg="#054907",fg="white",width=3,command=lambda: button_click(Button9))
Button9.grid(row=3,column=2)




main.mainloop()