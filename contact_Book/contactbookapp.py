import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
import mysql.connector as ms
from tkinter import messagebox
from tkinter import Tk, BOTH, Menu

class ContactBookApp:
    def clear(self,event):
        if self.name.get() == 'Name' : 
            self.name.delete(0,30)
    def clear1(self,event):
        if self.number.get() == 'Phone Number' : 
            self.number.delete(0,30)
    def clear2(self,event):
        if self.email.get() == 'Email' : 
            self.email.delete(0,30)
    def clear3(self,event):
        if self.landmark.get() == 'Landmark' : 
            self.landmark.delete(0,30)
    def clear4(self,event):
        if self.city.get() == 'City' : 
            self.city.delete(0,30)
    def clear5(self,event):
        if self.state.get() == 'State' : 
            self.state.delete(0,30)
        
            
     #delete the selected contact       
    def delete_check(self,num):
        ans = askyesno("CONTACT BOOk","Are you sure you want to delete this contact?")
        if ans:
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("Delete from Contact_List where number = '{}';".format(num))
            con.commit()
            con.close()
            
            self.open_contact_list()
            self.show_contact()
        
            
    #allowing Update
    def allow_update(self):
        self.name.configure(state="normal")
        self.number.configure(state="normal")
        self.email.configure(state="normal")
        self.landmark.configure(state="normal")
        self.city.configure(state="normal")
        self.state.configure(state="normal")
        self.done.configure(state="active",activebackground="#FFA500")
        
    
    #to search the contact whenever any character is entered on search bar.
    def search_contact(self,event):
        if self.search.get() == 'Search':
            self.search.delete(0,50)
        else:
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('select name,number from contact_list where name like "%{}%" or number like "%{}%";'.format(self.search.get(),self.search.get()))
            data=cur.fetchall()
            con.commit()
            con.close()

            data.sort(key=lambda a: a[0])
            for widget in self.scroll_frame.winfo_children():   #for deleting all Button present in frame
                if isinstance(widget, tk.Button):
                    widget.destroy()
            
            if not data :
                label = tk.Label(self.scroll_frame)
                label.configure(font=("Times New Roman",24),
                            foreground="#000000",
                            text="No Contact")
                label.place(height=40,width=300,x=0, y=0)
                return
                   
            text_list = []
            c=0
            for i in data :
                button = tk.Button(self.scroll_frame)
                button.config(command=lambda button=button:self.update_contact_details(button))
                button.configure(font="{Times New Roman} 15 {bold}",
                            anchor="w",
                            foreground="#000000",
                            text=i[0]+'  ['+i[1]+']')
                text_list.append(button)
                button.place(height=40,width=300,x=0, y=c*50)
                if c*50 < 420 :
                    self.scroll_frame.config(height=420,width=280)
                else :
                    self.scroll_frame.config(height=c*50+10,width=280)
                c += 1 
                
    # To get all the number present in database and show them on scrolled text.
    def show_contact(self,all_contact=False):
        if self.search.get() != 'Search':
            self.search.delete(0,30)
            self.search.insert("0","Search")
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select name,number from contact_list;')
        data=cur.fetchall()
        con.commit()
        con.close()
        if all_contact :
            data.sort(key=lambda a: a[0])
        if not data :
                label = tk.Label(self.scroll_frame)
                label.configure(font="{Times New Roman} 15 {bold}",
                            foreground="#000000",
                            text="No Contact")
                label.place(height=40,width=300,x=0, y=0)
                return
            
        text_list = []
        c=0
        for i in data :
            button = tk.Button(self.scroll_frame)
            button.config(command=lambda button=button:self.update_contact_details(button))
            button.configure(font="{Times New Roman} 15 {bold}",
                        anchor="w",
                        foreground="#000000",
                        text=i[0]+'  ['+i[1]+']')
            text_list.append(button)
            button.place(height=40,width=300,x=0, y=c*50)
            if c*50 < 420 :
                self.scroll_frame.config(height=420,width=280)
            else :
                self.scroll_frame.config(height=c*50+10,width=280)
            c += 1                

    #to add contact in the database               
    def contact_added(self):
        try:
            if len(self.number.get()) != 10:
                messagebox.showerror("Error","Invalid Phone Number")
                return
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('insert into Contact_List values( "{}","{}","{}","{}","{}","{}");'.format(self.name.get(),self.number.get(),self.email.get(),self.landmark.get(),self.city.get(),self.state.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Message","Successfully Added.")
            self.open_contact_list()
        except:
            messagebox.showerror("Error","Phone Number already saved")
            
    #to update selected contact in the database 
    def contact_updated(self,num):
        try:
            if len(self.number.get()) != 10:
                messagebox.showerror("Error","Invalid Phone Number")
                return
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("update Contact_List set name = '{}', number = '{}', email = '{}', landmark = '{}', city = '{}', state = '{}' where number = '{}';".format(self.name.get(),self.number.get(),self.email.get(),self.landmark.get(),self.city.get(),self.state.get(),num))
            con.commit()
            con.close()
            messagebox.showinfo("Message","Successfully Updated.")
            self.open_contact_list()
            self.show_contact()
        except:
            messagebox.showerror("Error","Invalid Phone Number")

        
    #getting full details of contact which is selected for updation
    def update_contact_details(self,v):
        var1 = v.cget("text").split()
        var = var1[-1][1:-1]
        #fetching from database
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select * from contact_list where number = "{}";'.format(var))
        data=cur.fetchall()
        con.commit()
        con.close()
        
        self.update_contact = tk.Frame(self.contact_book)
        self.update_contact.configure(background="#ffffff", height=550, width=300)
        

        self.setting = tk.Menubutton(self.update_contact) #menu button - to update and delete.
        self.img_three_dot = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\three_dot.png")
        self.setting.configure(
            background="#ffffff",
            font="{Calibri} 10 {bold}",
            foreground="#000000",
            cursor="hand2",
            borderwidth=0,
            image=self.img_three_dot)
        self.setting.place(anchor="nw", height=30, width=20, x=270, y=2)

        #menu
        self.setting.menu=Menu(self.setting,tearoff=0)
        self.setting["menu"]=self.setting.menu
        self.setting.menu.add_command(label='Update',
                                     background="#ffffff",
                                     font="{Calibri} 14 {}",
                                     foreground="#000000",
                                     command=self.allow_update)
        self.setting.menu.add_command(label='Delete',
                                     background="#ffffff",
                                     font="{Calibri} 14 {}",
                                     foreground="#000000",
                                     command=lambda:self.delete_check(var))
        

        # for design of icons and labels
        label101 = tk.Label(self.update_contact)
        self.img_name = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\name.png")
        label101.configure(background="#ffffff",image=self.img_name)
        label101.place(anchor="nw", height=35, width=35, x=10, y=120)

        label111 = tk.Label(self.update_contact)
        label111.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Name")
        label111.place(anchor="nw", height=22, width=40, x=50, y=105)

        label102 = tk.Label(self.update_contact)
        self.img_number = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\number.png")
        label102.configure(background="#ffffff",image=self.img_number)
        label102.place(anchor="nw", height=35, width=35, x=10, y=180)

        label121 = tk.Label(self.update_contact)
        label121.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Phone")
        label121.place(anchor="nw", height=22, width=40, x=50, y=165)
        
        label103 = tk.Label(self.update_contact)
        self.img_mail = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\mail.png")
        label103.configure(background="#ffffff",image=self.img_mail)
        label103.place(anchor="nw", height=35, width=35, x=10, y=240)

        label131 = tk.Label(self.update_contact)
        label131.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Email")
        label131.place(anchor="nw", height=22, width=40, x=50, y=225)

        label104 = tk.Label(self.update_contact)
        self.img_landmark = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\landmark.png")
        label104.configure(background="#ffffff",image=self.img_landmark)
        label104.place(anchor="nw", height=35, width=35, x=10, y=300)

        label141 = tk.Label(self.update_contact)
        label141.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Landmark")
        label141.place(anchor="nw", height=22, width=65, x=50, y=285)

        label105 = tk.Label(self.update_contact)
        self.img_city = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\city.png")
        label105.configure(background="#ffffff",image=self.img_city)
        label105.place(anchor="nw", height=35, width=35, x=10, y=360)

        label151 = tk.Label(self.update_contact)
        label151.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="City")
        label151.place(anchor="nw", height=22, width=40, x=50, y=345)


        label106 = tk.Label(self.update_contact)
        self.img_state = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\state.png")
        label106.configure(background="#ffffff",image=self.img_state)
        label106.place(anchor="nw", height=35, width=35, x=10, y=420)

        label121 = tk.Label(self.update_contact)
        label121.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="State")
        label121.place(anchor="nw", height=22, width=40, x=50, y=405)

        
        
        self.name = tk.Entry(self.update_contact) #Update Name
        self.name.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000",
            )
        self.name.insert("0",data[0][0])
        self.name.configure(state="readonly")
        self.name.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=135)
        
        self.number = tk.Entry(self.update_contact)    #Update Number
        self.number.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.number.insert("0",data[0][1])
        self.number.configure(state="readonly")
        self.number.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=195)
        
        self.email = tk.Entry(self.update_contact)    #Update Mail
        self.email.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.email.insert("0",data[0][2])
        self.email.configure(state="readonly")
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=255)
        
        self.landmark = tk.Entry(self.update_contact)    #Update Landmark
        self.landmark.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.landmark.insert("0",data[0][3])
        self.landmark.configure(state="readonly")
        self.landmark.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=310)
        
        self.city = tk.Entry(self.update_contact)    #Update City
        self.city.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.city.insert("0",data[0][4])
        self.city.configure(state="readonly")
        self.city.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=370)
        
        self.state = tk.Entry(self.update_contact)    #Update State
        self.state.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.state.insert("0",data[0][5])
        self.state.configure(state="readonly")
        self.state.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=430)
        
        separator20 = ttk.Separator(self.update_contact)           #for design
        separator20.configure(orient="horizontal")
        separator20.place(anchor="nw", width=240, x=50, y=160)
        separator21 = ttk.Separator(self.update_contact)
        separator21.configure(orient="horizontal")
        separator21.place(anchor="nw", width=240, x=50, y=220)
        separator22 = ttk.Separator(self.update_contact)
        separator22.configure(orient="horizontal")
        separator22.place(anchor="nw", width=240, x=50, y=280)
        separator23 = ttk.Separator(self.update_contact)
        separator23.configure(orient="horizontal")
        separator23.place(anchor="nw", width=240, x=50, y=340)
        separator24 = ttk.Separator(self.update_contact)
        separator24.configure(orient="horizontal")
        separator24.place(anchor="nw", width=240, x=50, y=400)
        separator25 = ttk.Separator(self.update_contact)
        separator25.configure(orient="horizontal")
        separator25.place(anchor="nw", width=240, x=50, y=460)
        
        self.back = tk.Button(self.update_contact)     #go back to home tab.
        self.back.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#000000",
            text='←',
            command = self.open_contact_list)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
        
        self.done = tk.Button(self.update_contact)     #add button - to add contact in database.
        self.done.configure(
            background="#FFA500",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text="Update & Continue",
            state="disabled",
            command = lambda:self.contact_updated(data[0][1]))
        self.done.place(anchor="nw", height=30, width=200, x=50, y=500)
        
        self.update_contact.place(anchor="nw", height=550, width=300, x=0, y=0)
    
    
    #This is " Contact list frame / Home frame " where list of all contact is shown or "No Contact" in case of empty contact list. 
    def open_contact_list(self):
        self.view_contact_list = tk.Frame(self.contact_book)
        self.view_contact_list.configure(
            background="#ffffff", height=550, width=300)

        label100 = tk.Label(self.view_contact_list)
        label100.configure(
            background="#ffffff",
            font="{Times New Roman} 20 {bold}",
            foreground="#000000",
            anchor='w',
            text='Contacts')
        label100.place(anchor="nw", height=40, width=250, x=0, y=0)

        self.add = tk.Button(self.view_contact_list) #Add button - to open add contact frame.
        self.add.configure(
            background="#ffffff",
            font="{Calibri} 25 {bold}",
            foreground="#000000",
            borderwidth=0,
            text='+',
            command=self.open_add_contact)
        self.add.place(anchor="nw", height=40, width=50, x=250, y=0)
        
        self.search = tk.Entry(self.view_contact_list)  #Search Bar - for searching contact by name or number
        self.search.configure(
            background="#e6e6e6",
            borderwidth=2,
            font="{Calibri} 14 {}",
            foreground="#000000")
        _text_ = 'Search'
        self.search.insert("0", _text_)
        self.search.place(anchor="nw",bordermode="inside",height=30, width=250, x=25, y=50)
        self.search.bind("<Button>",self.search_contact)
        self.search.bind("<KeyRelease>",self.search_contact)

        self.recent = tk.Button(self.view_contact_list) #Add button - to open add contact frame.
        self.recent.configure(
            background="#e6e6e6",
            font="{Calibri} 16 {bold}",
            foreground="#000000",
            borderwidth=1,
            text='Recent',
            command=lambda:self.show_contact(False)
            )
        self.recent.place(anchor="nw", height=30, width=70, x=45, y=90)

        self.all = tk.Button(self.view_contact_list) #Add button - to open add contact frame.
        self.all.configure(
            background="#e6e6e6",
            borderwidth=1,
            font="{Calibri} 16 {bold}",
            foreground="#000000",
            text='All Contacts',
            command=lambda:self.show_contact(True)
            )
        self.all.place(anchor="nw", height=30, width=110, x=150, y=90)
                

        self.scroll_frame = ctk.CTkScrollableFrame(self.view_contact_list,orientation="vertical")
        self.scroll_frame.configure(height=420,width=280)
        self.scroll_frame.config(background="#ffffff",height=420,width=280)
        self.scroll_frame.place(x=0, y=130)
        
        
        self.view_contact_list.place(
            anchor="nw", height=550, width=3000, x=0, y=0)
        
        self.show_contact() #this function is called to show all the contact present in database on scrolled text.

    #to add contact in the database.    
    def open_add_contact(self):
        self.add_contact = tk.Frame(self.contact_book)
        self.add_contact.configure(background="#ffffff", height=550, width=300)
        
        '''label14 = tk.Label(self.add_contact)
        label14.configure(
            background="#000000",
            font="{Arial} 12 {}",
            foreground="#ffffff",
            text='ADD CONTACT')
        label14.place(anchor="nw", height=25, width=120, x=65, y=0)'''
        

        # for design of icons and labels
        label101 = tk.Label(self.add_contact)
        self.img_name = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\name.png")
        label101.configure(background="#ffffff",image=self.img_name)
        label101.place(anchor="nw", height=35, width=35, x=10, y=120)

        label111 = tk.Label(self.add_contact)
        label111.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Name")
        label111.place(anchor="nw", height=22, width=40, x=50, y=105)

        label102 = tk.Label(self.add_contact)
        self.img_number = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\number.png")
        label102.configure(background="#ffffff",image=self.img_number)
        label102.place(anchor="nw", height=35, width=35, x=10, y=180)

        label121 = tk.Label(self.add_contact)
        label121.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Phone")
        label121.place(anchor="nw", height=22, width=40, x=50, y=165)
        
        label103 = tk.Label(self.add_contact)
        self.img_mail = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\mail.png")
        label103.configure(background="#ffffff",image=self.img_mail)
        label103.place(anchor="nw", height=35, width=35, x=10, y=240)

        label131 = tk.Label(self.add_contact)
        label131.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Email")
        label131.place(anchor="nw", height=22, width=40, x=50, y=225)

        label104 = tk.Label(self.add_contact)
        self.img_landmark = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\landmark.png")
        label104.configure(background="#ffffff",image=self.img_landmark)
        label104.place(anchor="nw", height=35, width=35, x=10, y=300)

        label141 = tk.Label(self.add_contact)
        label141.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="Landmark")
        label141.place(anchor="nw", height=22, width=65, x=50, y=285)

        label105 = tk.Label(self.add_contact)
        self.img_city = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\city.png")
        label105.configure(background="#ffffff",image=self.img_city)
        label105.place(anchor="nw", height=35, width=35, x=10, y=360)

        label151 = tk.Label(self.add_contact)
        label151.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="City")
        label151.place(anchor="nw", height=22, width=40, x=50, y=345)


        label106 = tk.Label(self.add_contact)
        self.img_state = tk.PhotoImage(file=r"C:\Users\Lenovo\Desktop\Programing\python\CodeSoft\contact_Book\state.png")
        label106.configure(background="#ffffff",image=self.img_state)
        label106.place(anchor="nw", height=35, width=35, x=10, y=420)

        label121 = tk.Label(self.add_contact)
        label121.configure(background="#e6e6e6",font="{Calibri} 11 {bold}",foreground="#000000",text="State")
        label121.place(anchor="nw", height=22, width=40, x=50, y=405)

        
        
        self.name = tk.Entry(self.add_contact) #Enter Name
        self.name.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.name.insert("0",'Name')
        self.name.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=135)
        self.name.bind('<Button>',self.clear)
        
        self.number = tk.Entry(self.add_contact)    #Enter Number
        self.number.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.number.insert("0",'Phone Number')
        self.number.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=195)
        self.number.bind('<Button>',self.clear1)
        
        self.email = tk.Entry(self.add_contact)    #Enter Mail
        self.email.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.email.insert("0",'Email')
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=255)
        self.email.bind('<Button>',self.clear2)
        
        self.landmark = tk.Entry(self.add_contact)    #Enter Landmark
        self.landmark.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.landmark.insert("0",'Landmark')
        self.landmark.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=310)
        self.landmark.bind('<Button>',self.clear3)
        
        self.city = tk.Entry(self.add_contact)    #Enter City
        self.city.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.city.insert("0",'City')
        self.city.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=370)
        self.city.bind('<Button>',self.clear4)
        
        self.state = tk.Entry(self.add_contact)    #Enter State
        self.state.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {}",
            foreground="#000000")
        self.state.insert("0",'State')
        self.state.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=240,
            x=50,
            y=430)
        self.state.bind('<Button>',self.clear5)
        
        separator20 = ttk.Separator(self.add_contact)           #for design
        separator20.configure(orient="horizontal")
        separator20.place(anchor="nw", width=240, x=50, y=160)
        separator21 = ttk.Separator(self.add_contact)
        separator21.configure(orient="horizontal")
        separator21.place(anchor="nw", width=240, x=50, y=220)
        separator22 = ttk.Separator(self.add_contact)
        separator22.configure(orient="horizontal")
        separator22.place(anchor="nw", width=240, x=50, y=280)
        separator23 = ttk.Separator(self.add_contact)
        separator23.configure(orient="horizontal")
        separator23.place(anchor="nw", width=240, x=50, y=340)
        separator24 = ttk.Separator(self.add_contact)
        separator24.configure(orient="horizontal")
        separator24.place(anchor="nw", width=240, x=50, y=400)
        separator25 = ttk.Separator(self.add_contact)
        separator25.configure(orient="horizontal")
        separator25.place(anchor="nw", width=240, x=50, y=460)
        
        self.back = tk.Button(self.add_contact)     #go back to home tab.
        self.back.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#000000",
            text='←',
            command = self.open_contact_list)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
        
        self.done = tk.Button(self.add_contact)     #add button - to add contact in database.
        self.done.configure(
            background="#FFA500",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='Save & Continue',
            command = self.contact_added)
        self.done.place(anchor="nw", height=30, width=200, x=50, y=500)
        
        self.add_contact.place(anchor="nw", height=550, width=300, x=0, y=0)

        
    def __init__(self, master=None):
        #build ui
        
        self.contact_book = tk.Tk() if master is None else tk.Toplevel(master)
        self.contact_book.configure(background="#ffffff",height=550, width=300)
        self.contact_book.resizable(False, False)
        self.contact_book.title("Contact Book")
        
        
        self.open_contact_list()    #Home tab
        
        # Main widget
        self.mainwindow = self.contact_book

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = ContactBookApp()
    app.run()
