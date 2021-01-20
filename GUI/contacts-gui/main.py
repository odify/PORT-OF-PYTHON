#!/usr/bin/env python3


from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('500x600')
root.title("Contacts GUI")
root.configure(background="#3DD7AC")




textin=StringVar()



exlist={
'Ali':'Ali Mohammad Musti\nali@mail.com\n01575-22930947717',
'Chris':'Cristian Tahle\nchris@mail.com\n01575-22930947751',
'Emily':'Emily Klass\nemi@mail.com\n01575-22930947752',
'Franco':'Franco da Silva\nfs@mail.com\n01575-22930947753',
'Guilia':'Guilia Monza\ngui@mail.com\n01575-22930947754',
'Laura':'Laura Siebert\nlssi@mail.com\n01575-22930947755',
'Mohammad':'Mohammad Mustiman\nmoma@mail.com\n01575-22930947756',
'Suna':'Suna Agyar\nsusa@mail.com\n01575-229309477577',
'Sameth':'Sameth Yilmaz\nsamy@mail.com\n01575-22930947758',
'Viviane':'Viviane Logan\nvivil@mail.com\n01575-22930947759'}



def clk():
     entered = ent.get()
     output.delete(0.0,END)
     try:
          textin = exlist[entered]
     except:
          textin = 'SORRY NO INFO \n AVAILABLE!!!!!!!!\n'
     output.insert(0.0,textin)

def ex():
   tkinter.messagebox.showinfo("Program",'Exit')
   exit()
     
def exitt():
     tkinter.messagebox.showinfo("Program",'Exit')
     exit()   

def me():
     text='\n WHAT? \n Ok Bro... \n Easy (Y)'
     saveFile=open('text.txt','w')
     saveFile.write(text)
     print('This are the entries::',text)
     
   
def hel():
   help(tkinter)

def cont():
     tkinter.messagebox.showinfo("Conatcts:",'\n 1.Ali\n 2.Chris \n 3.Emily \n 4.Franco \n 5.Guilia \n 6.Laura \n 7.Mohammad \n 8.Suna \n 6.Sameth \n 10.Viviane')
   
     
def clr():
     textin.set(" ")
     

menu = Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Memo",command=me)
subm.add_command(label="Save")
subm.add_command(label="Save As")
subm.add_command(label="Print")
subm.add_command(label="Exit",command=ex)

subm1 = Menu(menu)
menu.add_cascade(label="Contacts",menu=subm1)
subm1.add_command(label="to select:",command=cont)



lab=Label(root,text='Name :',font=('none 20 bold'))
lab.grid(row=0,column=1,sticky=W)


ent=Entry(root,width=20,font=('none 17 bold'),textvar=textin,bg='white')
ent.grid(row=0,column=2,sticky=W)


but=Button(root,padx=2,pady=2,text='Submit',command=clk,bg='powder blue',font=('none 18 bold'))
but.place(x=100,y=90)


but4=Button(root,padx=2,pady=2,text='Clear',font=('none 18 bold'),bg='powder blue',command=clr)
but4.place(x=220,y=90)



output=Text(root,width=20,height=8,font=('Time 20 bold'),fg="black")
output.place(x=100,y=200)


labb=Label(root,text='Results',font=('non 16 bold'))
labb.place(x=0,y=180)


but1=Button(root,padx=2,pady=2,text='Exit',command=exitt,bg='powder blue',font=('none 18 bold'))
but1.place(x=200,y=470)



root.mainloop()
