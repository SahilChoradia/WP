from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_Dosa.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_Pancakes.delete(0,END)
    entry_Pastries.delete(0,END)

def Total():
    try:a1=int(Dosa.get())
    except:a1=0

    try:a2=int(Cookies.get())
    except:a2=0

    try:a3=int(Tea.get())
    except:a3=0

    try:a4=int(Coffee.get())
    except:a4=0

    try:a5=int(Juice.get())
    except:a5=0

    try:a6=int(Pancakes.get())
    except:a6=0

    try:a7=int(Pastries.get())
    except:a7=0

    c1=60*a1
    c2=10*a2
    c3=10*a3
    c4=20*a4
    c5=40*a5
    c6=120*a6
    c7=80*a7

    lbl_Total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_Total.place(x=0,y=50)

    Entry_Total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    Entry_Total.place(x=20,y=100)

    Totalcost=c1+c2+c3+c4+c5+c6+c7
    String_Bill="Rs.",str('%2f'%Totalcost)
    Total_bill.set(String_Bill)
    

       
Label(text="Bill Management",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#M#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width="300",height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies......Rs.10/piece",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea......Rs.10/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee......Rs.20/cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice......Rs.40/glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes......Rs.110",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pastries......Rs.80/piece",fg="black",bg="lightgreen").place(x=10,y=260)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("Calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)


#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pancakes=StringVar()
Pastries=StringVar()
Total_bill=StringVar()

#Label
lbl_Dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_Cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
lbl_Coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue4")
lbl_Juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")
lbl_Pancakes=Label(f1,font=("aria",20,'bold'),text="Pancakes",width=12,fg="blue4")
lbl_Pastries=Label(f1,font=("aria",20,'bold'),text="Pastries",width=12,fg="blue4")

lbl_Dosa.grid(row=1,column=0)
lbl_Cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Coffee.grid(row=4,column=0)
lbl_Juice.grid(row=5,column=0)
lbl_Pancakes.grid(row=6,column=0)
lbl_Pastries.grid(row=7,column=0)


#Entry
entry_Dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_Coffee=Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg="lightpink")
entry_Juice=Entry(f1,font=("aria",20,'bold'),textvariable=Juice,bd=6,width=8,bg="lightpink")
entry_Pancakes=Entry(f1,font=("aria",20,'bold'),textvariable=Pancakes,bd=6,width=8,bg="lightpink")
entry_Pastries=Entry(f1,font=("aria",20,'bold'),textvariable=Pastries,bd=6,width=8,bg="lightpink")




entry_Dosa.grid(row=1,column=1)
entry_Cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Coffee.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_Pancakes.grid(row=6,column=1)
entry_Pastries.grid(row=7,column=1)

#buttons
btn_Reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_Reset.grid(row=8,column=0)

btn_Total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_Total.grid(row=8,column=1)




root.mainloop()
