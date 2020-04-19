import tkinter as tk
from tkinter import *
import time
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
global database
win=tk.Tk()
#database=""
database=""
#########    ALL    VARIABLE    ##############################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
data_base=tk.StringVar()
cal_price=tk.DoubleVar()
cal_gst=tk.DoubleVar()
cal_amt=tk.DoubleVar()
cal_item=tk.StringVar()
cal_qut=tk.DoubleVar()
cal_id=tk.IntVar()
global datalist
global bill

global d
global bill_list
bill_list=[]
datalist=[]
Add_item=tk.StringVar()
price=tk.DoubleVar()
create_new_data=tk.StringVar()
getdatabase=""
d=""
yes=0
global l
l=[]
customer=tk.StringVar()
phone=tk.StringVar()

new_item=tk.StringVar()

new_price=tk.DoubleVar()

new_gst=tk.DoubleVar()

new_qunt=tk.DoubleVar()

new_id=tk.IntVar()















#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def removewin():
    global win
    for widget in win.winfo_children():
        widget.grid_remove()
        
def loginpage():
    
    #top1=Toplevel()
    win.minsize(1350,2000)
    user=tk.StringVar()
    password=tk.StringVar()
    
   #border=tk.Canvas(win,width=1000,height=1000)
    admin=tk.Label(win,text="Admin_login",font=("Arial Bold", 38))
    admin.grid(row=0,column=0, columnspan=1,pady=(0,0),padx=(70,0))
    
    username=tk.Label(win,text="Username",font=("Arial Bold", 18))
    username.grid(row=1,column=0,pady=(100,0),padx=(30,0))
    enter_user=ttk.Entry(win,textvariable=user)
    enter_user.grid(row=1,column=1,pady=(100,0),padx=(30,0))
    
    pasword=tk.Label(win,text="Password",font=("Arial Bold", 18))
    pasword.grid(row=2,column=0,pady=(10,0),padx=(30,0))
    enter_pass=ttk.Entry(win,textvariable=password,show="*")
    enter_pass.grid(row=2,column=1,pady=(10,0),padx=(30,0))
    def login():
        us=user.get()
        ps=password.get()
        if us=="admin" and ps =="admin":
            removewin()
            select_data_base_window()
        else:
            tk.messagebox.showerror("ERROR","invalid user or password")
    logbtn=ttk.Button(win,text="Login",command=login)
    logbtn.grid(row=3,column=0,pady=(10,0),padx=(60,0))
    
def dada_base_info():
    global d
    d=data_base.get()
    if d=="":
        tk.messagebox.showerror("warning","select database")
    else:
        #datalist.append(d)
        #database=data.get()
       ## conn=sqlite3.connect(database+ext)
       # cur=conn.cursor()
        #if d not in dalalist:
          #  pass
            
        main_task()
#-------------------------------------------------------------------------------------------------------------------------------------------------        
def take_items_from_database():
    global datalist
    global d
    datalist=[]
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    sql=""" SELECT itemname FROM item"""
    cur.execute(sql)
    find=cur.fetchall()
    for i in find:
        datalist.extend(i)

    



        
#---------------------------------------------------------------------------------------------------------------------------------------------------


        
def calculate_bill():
    global d
    global cal_item
    global cal_qut
    global cal_gst
    global l
    global bill
    global bill_list
    global show_sales
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getitem=cal_item.get()
    q=float(cal_qut.get())
    print(getitem,q)
    if getitem !=""and q!=0:
        
        
        
        cur.execute('SELECT id, price,gst FROM item WHERE itemname=?',(getitem,))
        acorrding_item=cur.fetchone()
        
        gst=float(acorrding_item[2])
        print(acorrding_item,gst)
        gst=gst*q
    
        amount=acorrding_item[1]
        amount=amount*q
        addgst=(amount*gst)/100
        amount=amount+addgst

    
        cal_price.set(amount)
        cal_id.set(acorrding_item[0])
        cal_gst.set(gst)
        l=[]
        a=cal_price.get()
        b=cal_item.get()
        c=cal_gst.get()
        date=datetime.date.today()
        customer_name=customer.get()
        pho=phone.get()
        bill_list=cal_item.get(),cal_gst.get(),cal_price.get()
        detail=[customer_name,pho]
        cur.execute('INSERT INTO daleysales(date,customername,itemname,totalquantity,totalprice,totalgst)VALUES(?,?,?,?,?,?)',(date,customer_name,b,q,a,c))
        conn.commit()
        if yes==0:
            bill.insert(END,detail,'\n')
            bill.insert(END,bill_list)
        
        
        
    
    else:
        tk.messagebox.showerror('Warning','fill qty or itm')
    

def description():
    global d
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getdata=cal_item
    if getdata!="":
        pass
        
#===================================================================================================================================================
    

def select_data_base_window():
    win.minsize(1350,2000)
    newbutton=tk.Button(win,text="New",font=("Arial Bold", 18),height=2,width=4,command=new_database)
    newbutton.grid(row=0,column=0,padx=1200,pady=10)
    frame1=tk.Label(win,bd=10,bg="goldenrod")
    frame1.place(x=400,y=60,height=500,width=500)
    datainfo=tk.Label(frame1,text="SELECT  YOUR  DATA_BASE", bg='DarkSeaGreen4', font=("Arial Bold", 24))
    datainfo.grid(row=0,column=0,padx=10,pady=3)
    data=ttk.Combobox(frame1,width=20,textvariable=data_base,font=("Arial Bold", 18))
    data["values"]=datalist
    data.grid(row=1,column=0,padx=20,pady=40)
    button=tk.Button(frame1,text="process",font=("Arial Bold", 18),command=dada_base_info)
    button.grid(row=2,column=0,padx=10,pady=10)
    info=tk.Label(frame1,text="Welcome Users", bg='DarkSeaGreen4', font=("Arial Bold", 24), width=15,height=5)
    info.grid(row=3,column=0,padx=10,pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def new_database():
    call_new()
    
def call_new():
    top=Toplevel(win,bg="medium spring green")
    top.minsize(1350,2000)
    frame2=Frame(top,bd=20,bg="lemon chiffon")
    frame2.place(x=200,y=100,width=1000,height=1000)
    name=tk.Label(frame2,text="Create your NewDataBase",font=("Arial Bold",28),width=25,height=3,bg="steel blue")
    name.grid(row=0,column=0,padx=230,pady=10)
    data_enter=ttk.Entry(frame2,width=25,textvariable=data_base,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=0,pady=10)
    databas=tk.Button(frame2,text="create DataBase",font=("Arial Bold", 24),command=create)
    databas.grid(row=2,column=0,columnspan=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    
    
















    
    
def mainwindow():
    #win=tk.Tk()
    top=Toplevel(win)
    top.minsize(1350,2000)
    border=tk.Canvas(top,width=1000,height=1000)
    border.pack()
    frame1=tk.Frame(top,bd=10,bg="crimson")
    frame1.place(x=0,y=0,width=1000,height=100)
    frame2=tk.Frame(top,bd=10,bg="")
    frame2.place(x=0,y=100,width=500,height=1000)

    data=tk.StringVar()
    data_enter=ttk.Entry(frame1,width=25,textvariable=data,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=2)
    
#'''def ck():
   # database=data.get()
    #ext=".db"
    #conn=sqlite3.connect(database+ext)
    #cur=conn.cursor()
    #print(database)'''
    item=tkinter.Label(frame2,text='Item name',font=("Arial Bold", 18))
    item.grid(row=0,column=0)
    tmenter=tk.StringVar()

    item_enter=tk.Entry(frame2,textvariable=tmenter,bd=10)
    item_enter.grid(row=0,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=2,column=0)

    price=tkinter.Label(frame2,text='Price         ',font=("Arial Bold", 18))
    price.grid(row=3,column=0)

    penter=tk.StringVar()

    price_enter=tk.Entry(frame2,textvariable=penter,bd=10)
    price_enter.grid(row=3,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=4,column=0)


    brand=tkinter.Label(frame2,text='brand          ',font=("Arial Bold", 18))
    brand.grid(row=5,column=0)

    benter=tk.StringVar()
    i=data_base.get()

    

    benter.set(i)

    brand_enter=tk.Entry(frame2,text=benter,bd=10)
    brand_enter.grid(row=5,column=5)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    global d
    d=data_base.get()
    if d!="":
        try:
            
            ext=".db"
            conn=sqlite3.connect(d+ext)
            cur=conn.cursor()
            table1="""CREATE TABLE item(id int PRIMARY KEY ,itemname char UNIQUE ,price float, gst float,quantity float,date )"""
            cur.execute(table1)
            #if checkl!=True:
                
            #ans=tk.messagebox.showerror('warning','SOMETHING WRONG')

                
            table2="""CREATE TABLE daleysales(date,customername char,itemname,totalquantity,totalprice float,totalgst float)"""
            check2=cur.execute(table2)
            #if check2!=True:
                
            ##ans=tk.messagebox.showerror('warning','SOMETHING WRONG')
            main_task()        
        except Exception as e:
             
             tk.messagebox.showerror("Warning","database already exist")

    else:
        ans=tk.messagebox.showerror('warning','YOU have fill the option')
            
    #take_items_from_database()
   # databas=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=create)
    #databas.grid(row=1,column=0,columnspan=1)
     #

     #database2=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=ck)
     #database2.grid(row=1,column=3,columnspan=3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






def main_task():
    global bill
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    but_1=Button(wi, text='Add item', width=12, bg='brown', fg='white', command=open_win).grid(row=0, column=0, padx=10)
    but_2=Button(wi, text='Update item', width=12, bg='brown', fg='white', command=open_win2).grid(row=0, column=1, padx=10)
    but_3=Button(wi, text='Sales as per product', width=20, bg='brown', fg='white', command=open_win3).grid(row=0, column=2, padx=10)
    but_4=Button(wi, text='Sales as per day', width=20, bg='brown', fg='white', command=open_win4).grid(row=0, column=3, padx=10)
    try:
        
        take_items_from_database()
    except :
        tk.messagebox.showerror("error","something wrong")

    Frame4 = Frame(wi, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="sky blue")
    Frame4.place(x=0, y=60, width=1600,height=80)
    lbl = Label(Frame4, font=( 'aria' ,28, 'bold' ),text="BILLING SYSTEM",fg="BLACK",bd=5,)
    lbl.grid(row=0,column=0,padx=500)


    Frame1 = Frame(wi, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="sky blue")
    Frame1.place(x=0, y=140, width=900,height=500)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #new
    lbl = Label(Frame1, font=( 'aria' ,16, 'bold' ),text="Customer Name-",fg="black",bd=6)
    lbl.grid(row=0,column=0,padx=2, pady=2)
    txt = Entry(Frame1,font=('ariel' ,16,'bold'),textvariable=customer,bg="white",width=15)
    txt.grid(row=0,column=1,padx=30,pady=1)
    global l
    l=[9,9,9,9,]

    lbl=Label(Frame1,text='Phone no.-',font=('arial',16,'bold'),bd=6,fg="black")
    lbl.grid(row=0,column=3,padx=1, pady=1)
    txt = Entry(Frame1,font=('ariel' ,16,'bold'),textvariable=phone,bg="white",width=15)
    txt.grid(row=0,column=4,padx=1,pady=1)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    lbl= Label(Frame1, font=( 'aria' ,14, 'bold' ),text="Item name-",fg="black",bd=5,width=13)
    lbl.grid(row=1,column=0,pady=(70,0))
    combobox = ttk.Combobox(Frame1, values=datalist,textvariable=cal_item ,width=24,state="readonly",font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=1,column=1,padx=(13,0),pady=(70,0))

    lbl = Label(Frame1, font=( 'aria' ,14, 'bold' ),text="Quantity->",fg="black",bd=5,width=8)
    lbl.grid(row=1,column=3,padx=60,pady=(70,0))
    combobox = tk.Entry(Frame1, textvariable=cal_qut,width=28,font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=1,column=4,pady=(70,0))


    lbl = Label(Frame1, font=( 'aria' ,16, 'bold' ),text="Gst->",fg="black",bd=5,width=13)
    lbl.grid(row=2,column=0,padx=0, pady=(70,0))
    txt = Entry(Frame1,font=('ariel' ,16,'bold'),textvariable=cal_gst,bg="white",width=15,state="readonly")
    txt.grid(row=2,column=1,pady=(70,0))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#new
    lbl=Label(Frame1,text='Price->',font=('arial',16,'bold'),bd=6,width=8,fg="black",)
    lbl.grid(row=2,column=3,padx=0,pady=(70,0))
    txt = Entry(Frame1,font=('ariel' ,16,'bold'),textvariable=cal_price,bg="white",state="readonly",width=15)
    txt.grid(row=2,column=4,padx=0,pady=(70,0))
    box = Listbox(Frame1, width=140, height=5).place(x=0,y=390)
    

    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    but_1=Button(Frame1, text='Enter', width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white',command=calculate_bill).grid(row=60, column=3, padx=1, pady=50)


    Frame2 = Frame(wi, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="sky blue")
    Frame2.place(x=927, y=140, height=500, width=430)

   # recipts = Listbox(Frame2, width=60, height=20)
    
    #recipts.grid(row=0, column=0, padx=10)#.place(x=40, y=50)

    #recipts.insert('end',l)
    bill=Text(Frame2,width=60, height=20)
    bill.grid(row=0, column=0, padx=2)
    
    but_1=Button(Frame2, text='Total', width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=50, column=0, padx=10,pady=20)
    but_1=Button(Frame2, text='Print', width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=60, column=0, padx=10)
    


    Frame5 = Frame(wi, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="sky blue")
    Frame5.place(x=0, y=640, width=1600,height=80)
    lbl = Label(Frame5, font=( 'Monotype Corsiva' ,14, 'bold' ),text='designed by UNICO Team')
    lbl.grid(row=0,column=0,padx=550)

    











    
   
#=================================================================================================================================================================    

def open_win():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    frame2=Frame(wi, bd=20, bg="lemon chiffon")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Add Product Details")
    label_1=Label(frame2,text='Add Product Details', relief="solid", font=('arial',12,'bold')).grid(row=0, column=15, padx=0, pady=0)#.place(x=670,y=100) 
    l2=Label(frame2,text='Product ID',font=('arial',12,'bold')).grid(row=1, column=10, padx=150, pady=25)#.place(x=600,y=200)
    e2=Entry(frame2,textvariable=new_id, bd=5,width=35).grid(row=1, column=50, padx=0, pady=0)#.place(x=750,y=200)
    
    l3=Label(frame2,text='Product Name',font=('arial',12,'bold')).grid(row=2, column=10, padx=0, pady=25)#.place(x=600,y=225)
    e3=Entry(frame2, textvariable=new_item,bd=5,width=35).grid(row=2, column=50, padx=0, pady=0)#.place(x=750,y=225)
    
    l4=Label(frame2,text='Quantity',font=('arial',12,'bold')).grid(row=3, column=10, padx=0, pady=25)#.place(x=600,y=250)
    e4=Entry(frame2,textvariable=new_qunt ,bd=5,width=35).grid(row=3, column=50, padx=0, pady=0)#.place(x=750,y=250)
 
    l5=Label(frame2,text='Price',font=('arial',12,'bold')).grid(row=4, column=10, padx=0, pady=25)#.place(x=600,y=275)
    e5=Entry(frame2,textvariable=new_price, bd=5,width=35).grid(row=4, column=50, padx=0, pady=0)#.place(x=750,y=275)
   
    l6=Label(frame2,text='GST',font=('arial',12,'bold')).grid(row=5, column=10, padx=0, pady=25)#.place(x=600,y=300)
    e6=Entry(frame2,textvariable=new_gst, bd=5,width=35).grid(row=5, column=50, padx=0, pady=0)#.place(x=750,y=300)
    but_1=Button(frame2, text='Submit', width=12, bg='brown', fg='white',command=add_item).grid(row=6, column=15, padx=0, pady=0)#.place(x=700, y=500)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 
    
def open_win2():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Add Product Details")
    frame2=Frame(wi, bd=20, bg="lemon chiffon")
    frame2.place(x=200, y=100, width=1000, height=500)
    label_1=Label(frame2,text='Update item', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=300, pady=10,columnspan=25)#.place(x=725,y=100)

    
    l2=Label(frame2,text='Product ID',font=('arial',12,'bold')).grid(row=1, column=0, padx=2, pady=25)#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35).grid(row=1, column=1, padx=0, pady=0)#.place(x=780,y=200)
    
    l3=Label(frame2,text='Product Name',font=('arial',12,'bold')).grid(row=2, column=0, padx=2, pady=25)#.place(x=600,y=225)
    e3=Entry(frame2, bd=5,width=35).grid(row=2, column=1, padx=0, pady=0)#.place(x=780,y=225)
    
    l4=Label(frame2,text='Quantity Available',font=('arial',12,'bold')).grid(row=3, column=0, padx=2, pady=25)#.place(x=600,y=250)
    e4=Entry(frame2, bd=5,width=35).grid(row=3, column=1, padx=0, pady=0)#.place(x=780,y=250)
 
    l5=Label(frame2,text='Quantity Purchased',font=('arial',12,'bold')).grid(row=4, column=0, padx=2, pady=25)#.place(x=600,y=275)
    e5=Entry(frame2, bd=5,width=35).grid(row=4, column=1, padx=0, pady=0)#.place(x=780,y=275)
   
    but_1=Button(frame2, text='Submit', width=12, bg='brown', fg='white').grid(row=5, column=0, padx=200, pady=25)#.place(x=700, y=500)    
    but_2=Button(frame2, text='Search', width=12, bg='brown', fg='white').grid(row=5, column=1, padx=0, pady=25)#.place(x=800, y=500)
#======================================================================================================================================================================
def open_win3():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    frame2=Frame(wi, bd=20, bg="lemon chiffon")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Sales as per product")
    label_1=Label(frame2,text='Sales as per product', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=0, pady=0)#.place(x=670,y=100) 
    l2=Label(frame2,text='Product ID',font=('arial',12,'bold')).grid(row=1, column=0, padx=0, pady=0)#.place(x=650,y=200)
    combobox = ttk.Combobox(frame2, values=["****", "****", "****","****"]).grid(row=1, column=1, padx=0, pady=0)#.place(x=750,y=200)
    box = Listbox(frame2, width=125)
    box.grid(row=2, column=0, padx=0, pady=0)#.place(x=360, y=300)
    but_1=Button(frame2, text='Export to excel', width=12, bg='brown', fg='white').grid(row=3, column=0, padx=0, pady=0)#.place(x=700, y=500)
#==================================================================================================================================================================
def open_win4():
    global show_sales
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Sales as per day")
    frame2=Frame(wi, bd=20, bg="lemon chiffon")
    frame2.place(x=200, y=100, width=1000, height=500)
    label_1=Label(frame2,text='Sales as per day', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=0, pady=0)#.place(x=670,y=100)
    l3=Label(frame2,text='From',font=('arial',12,'bold')).grid(row=1, column=0, padx=0, pady=0)#.place(x=400,y=200)
    e3=Entry(frame2, bd=5, width=35).grid(row=1, column=1, padx=0, pady=0)#.place(x=450,y=200)
    l4=Label(frame2,text='To',font=('arial',12,'bold')).grid(row=2, column=0, padx=0, pady=0)#.place(x=800,y=200)
    e4=Entry(frame2, bd=5, width=35).grid(row=2, column=1, padx=0, pady=0)#.place(x=829,y=200)
    show_sales = Text(frame2, width=125,height=50)
    show_sales.grid(row=3, column=0, padx=0, pady=0)#.place(x=360, y=300)
    but_1=Button(frame2, text='Export to excel', width=12, bg='brown', fg='white').grid(row=4, column=0, padx=0, pady=0)#.place(x=700, y=500)
    seles_daley()

  
    


def add_item():
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    price=new_price.get()
    Id=new_id.get()
    item=new_item.get()
    gst=new_gst.get()
    qunt=new_qunt.get()
    date="2020"
    if item!="" and Id!="" and price!="" and qunt!="" and gst!="":
        
        
        #print(d)
        cur.execute('INSERT INTO item(id,itemname,price,gst,quantity,date)VALUES(?,?,?,?,?,?)',(Id,item,price,gst,qunt,date))
        conn.commit()
        #conn.close()
        take_items_from_database() 
        
            
        #tk.messagebox.showerror('Error','you have an Error  at time add new item')
            
    else:
        tk.messagebox.showerror('Warning','you have to fill all option')
            
        
    
def update_item():
    
    pass
def delete_item():
    pass






def seles_daley():
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    date="20/12/2020"
    res=cur.execute("SELECT *FROM daleysales WHERE date=?",(date,))
    for i in res:
        show_sales.insert(END,i)
    
    
    











#######################################################################################################################################################################







     
#mainwindow()
loginpage()
#select_data_base_window()     
#call_new()
#main_task()

win.mainloop()
 
