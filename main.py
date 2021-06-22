from tkinter import *
from tkinter import messagebox as tmsg
root=Tk()

def click(event):
    global value,s,a,i,flag,text
    if flag==0:
        text=event.widget.cget("text")
    if value.get()=="0":
        textBox.delete(0,END)
        #textBox.insert(0,text)
    if text!="=" and text!="Del" and text!="sqrt" and text!="C":
        a=a+text
    #if len(a)>=18:
        #if int(a)>=10**17:
            #tmsg._show("Storage Error","Value too large to process")
            #flag=1
            #textBox.delete(0,END)
            #flag=0
    if text=="=":
        try:
            b=eval(a)
            a=""
            a=a+str(b)
            value.set(str(b))
        except:
            tmsg._show("ERROR","SYNTAX ERROR")
            value.set("0")
            a=""
    elif text=="Del":
        a=a[:len(a)-1]
        if a=="":
            value.set("0")
        else:
            value.set(a)
        flag=0
    elif text=="C":
        a=""
        value.set(a)
        flag=0
        textBox.insert(0,"0")
    elif text=="sqrt":
        a=a+"**(1/2)"
    else:
        if flag==0:
            if len(value.get()+text) > 19:
                tmsg._show("Error","Overflow")
            else:
                value.set(value.get()+text)
s=0
a=""
i=0
flag=0
text=""
root.resizable(width=False,height=False)
root.title("Calculator")
#mainmenu=Menu(root)
#m1=Menu(mainmenu,tearoff=0)
#m1.add_command(label="Copy",command=copy)
#m1.add_command(label="Cut",command=cut)
#m1.add_command(label="Paste",command=paste)
#mainmenu.add_cascade(label="Edit",menu=m1)
#root.config(menu=mainmenu)

#entry widget
value=StringVar()
textBox=Entry(root,font="lucinda 25 bold",textvariable=value,justify=RIGHT,borderwidth=0,relief=RAISED)
textBox.grid(row=0,column=0,columnspan=5)

#defining buttons
buttonC=Button(root,text="C",font="lucinda 18",borderwidth=0,relief=RAISED,width=5,fg="white",bg="black")
buttonMOD=Button(root,text="%",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonDEL=Button(root,text="Del",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonDIV=Button(root,text="/",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button7=Button(root,text="7",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button8=Button(root,text="8",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button9=Button(root,text="9",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonMUL=Button(root,text="*",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button4=Button(root,text="4",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button5=Button(root,text="5",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button6=Button(root,text="6",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonSUB=Button(root,text="-",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button1=Button(root,text="1",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button2=Button(root,text="2",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button3=Button(root,text="3",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonPLUS=Button(root,text="+",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button00=Button(root,text="sqrt",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
button0=Button(root,text="0",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonPOINT=Button(root,text=".",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)
buttonEQUALS=Button(root,text="=",font="lucinda 18",borderwidth=0,relief=RAISED,width=5)

#packing buttons into grid
buttonC.grid(row=1,column=0,sticky="NWNESWSE")
buttonMOD.grid(row=1,column=1,sticky="NWNESWSE")
buttonDEL.grid(row=1,column=2,sticky="NWNESWSE")
buttonDIV.grid(row=1,column=3,sticky="NWNESWSE")
button7.grid(row=2,column=0,sticky="NWNESWSE")
button8.grid(row=2,column=1,sticky="NWNESWSE")
button9.grid(row=2,column=2,sticky="NWNESWSE")
buttonMUL.grid(row=2,column=3,sticky="NWNESWSE")
button4.grid(row=3,column=0,sticky="NWNESWSE")
button5.grid(row=3,column=1,sticky="NWNESWSE")
button6.grid(row=3,column=2,sticky="NWNESWSE")
buttonSUB.grid(row=3,column=3,sticky="NWNESWSE")
button1.grid(row=4,column=0,sticky="NWNESWSE")
button2.grid(row=4,column=1,sticky="NWNESWSE")
button3.grid(row=4,column=2,sticky="NWNESWSE")
buttonPLUS.grid(row=4,column=3,sticky="NWNESWSE")
button00.grid(row=5,column=0,sticky="NWNESWSE")
button0.grid(row=5,column=1,sticky="NWNESWSE")
buttonPOINT.grid(row=5,column=2,sticky="NWNESWSE")
buttonEQUALS.grid(row=5,column=3,sticky="NWNESWSE")


#binding buttons for event
buttonC.bind('<Button-1>',click)
buttonMOD.bind('<Button-1>',click)
buttonDEL.bind('<Button-1>',click)
buttonDIV.bind('<Button-1>',click)
buttonMUL.bind('<Button-1>',click)
buttonSUB.bind('<Button-1>',click)
buttonPLUS.bind('<Button-1>',click)
buttonPOINT.bind('<Button-1>',click)
buttonEQUALS.bind('<Button-1>',click)
button7.bind('<Button-1>',click)
button8.bind('<Button-1>',click)
button9.bind('<Button-1>',click)
button4.bind('<Button-1>',click)
button5.bind('<Button-1>',click)
button6.bind('<Button-1>',click)
button1.bind('<Button-1>',click)
button2.bind('<Button-1>',click)
button3.bind('<Button-1>',click)
button00.bind('<Button-1>',click)
button0.bind('<Button-1>',click)
root.mainloop()
