from tkinter import *
from tkinter import messagebox
main= Tk()
main.title("TIC TAC TOE")

Button1=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button1.grid(row=0,column=0)
Button2=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button2.grid(row=0,column=1)
Button3=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button3.grid(row=0,column=2)
Button4=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button4.grid(row=0,column=0)
Button5=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button5.grid(row=0,column=1)
Button6=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button6.grid(row=0,column=3)
Button7=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button7.grid(row=0,column=0)
Button8=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button8.grid(row=0,column=1)
Button9=Button(main,text="",font=("arial",60,"bold"),bg="#054907",fg="black",width=3)
Button9.grid(row=0,column=3)




main.mainloop()

def printboard():
    pass

print("WELCOME TO TIC TAC TOE!!")
print(f" 0 | 1 | 2")
print(f"---|---|---")
print(f" 3 | 4 | 5")
print(f"---|---|---")
print(f" 6 | 7 | 8")

