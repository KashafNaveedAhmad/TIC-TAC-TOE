
from tkinter import *
from tkinter import messagebox

def button_click(Button):
    global x_o,flag
    Button["bg"]="#0d1d2b"
    if Button["text"]== "" and x_o==True:
        Button["text"]= "X"
        x_o = False
        check_wins()
        flag=flag+1
    elif Button["text"] == "" and x_o==False:
        Button["text"]="O"
        x_o = True
        check_wins()
        flag=flag+1    
    else:
        messagebox.showinfo("TIC TAC TOE ","Player already entered!")    
    
def check_wins():
    global Button1,Button2,Button3,Button4,Button5,Button6,Button7,Button8,Button9
    
    if Button1["text"]=="X"and Button2["text"]=="X"and Button3["text"]=="X" or Button4["text"]=="X"and Button5["text"]=="X"and Button6["text"]=="X" or Button7["text"]=="X"and Button8["text"]=="X"and Button9["text"]=="X"or Button3["text"]=="X"and Button5["text"]=="X"and  Button7["text"]=="X" or Button1["text"]=="X"and Button5["text"]=="X"and Button9["text"]=="X" or Button2["text"]=="X"and Button5["text"]=="X"and Button8["text"]=="X":
        messagebox.showinfo("TIC TAC TOE ","PLAYER 1 WINS!!")
    elif Button1["text"]=="O"and Button2["text"]=="O"and Button3["text"]=="O"or Button4["text"]=="O"and Button5["text"]=="O"and Button6["text"]=="O"or Button7["text"]=="O"and Button8["text"]=="O"and Button9["text"]=="O"or Button3["text"]=="O"and Button5["text"]=="O" and Button7["text"]=="O"or Button1["text"]=="O"and Button5["text"]=="O"and Button9["text"]=="O" or Button2["text"]=="O"and Button5["text"]=="O"and Button8["text"]=="O":
        messagebox.showinfo("TIC TAC TOE ","PLAYER 2 WINS!!")
    elif flag==8:
        messagebox.showinfo("TIC TAC TOE ","TIE!!")  
main=Tk()
main.title("TIC TAC TOE") 

x_o=True
flag=0

Button1=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button1))
Button1.grid(row=0,column=0)
Button2=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button2))
Button2.grid(row=0,column=1)
Button3=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button3))
Button3.grid(row=0,column=2)
Button4=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button4))
Button4.grid(row=1,column=0)
Button5=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button5))
Button5.grid(row=1,column=1)
Button6=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button6))
Button6.grid(row=1,column=2)
Button7=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button7))
Button7.grid(row=3,column=0)
Button8=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button8))
Button8.grid(row=3,column=1)
Button9=Button(main,text="",font=("arial",45,"bold"),bg="#1d3f5c",fg="grey",width=3,command=lambda: button_click(Button9))
Button9.grid(row=3,column=2)

     
       
main.mainloop()

