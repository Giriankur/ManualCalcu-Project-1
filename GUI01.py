from tkinter import *
def btnClick(number):
          global val
          val=val+str(number)
          data.set(val)
def btnClear():
        global val
        val = ""
        data.set("")
def btnEquals():
        global val
        result = str(eval(val))
        data.set(result)
root = Tk()
root.title("My calci Ankur Giri")
root.geometry("361x461+1000+200")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=30,justify="right",bg= "powder blue",font=("Ariel",20))
display.grid(row=0,columnspan=8)

btn1=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
btn1.grid(row=2,column=0)
btn2=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
btn2.grid(row=2,column=1)
btn3=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
btn3.grid(row=2,column=2)
btn_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btn_mul.grid(row=2,column=3)
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=3,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=3,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=3,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'))
btn_add.grid(row=3,column=3)
btn8=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
btn8.grid(row=4,column=0)
btn9=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
btn9.grid(row=4,column=1)
btn_1=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
btn_1.grid(row=4,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('-'))
btn_sub.grid(row=4,column=3)
btn_point=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,height=2,bg = "red",width=6,command=btnClear)
btn_point.grid(row=5,column=0)
btn_4=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
btn_4.grid(row=5,column=1)
btn_Equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btn_Equal.grid(row=5,column=2)
btn_Div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'))
btn_Div.grid(row=5,column=3)

root.mainloop()