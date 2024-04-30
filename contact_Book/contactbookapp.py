#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
import mysql.connector as ms
from tkinter import messagebox

class ContactBookApp:
    def clear(self,event):
        self.name.delete(0,30)
    def clear1(self,event):
        self.number.delete(0,30)
    def clear2(self,event):
        self.email.delete(0,30)
    def clear3(self,event):
        self.landmark.delete(0,30)
    def clear4(self,event):
        self.city.delete(0,30)
    def clear5(self,event):
        self.state.delete(0,30)
        

    # check wheater any contact is selected for updation or not and update button is activated accordingly
    def update_check(self,var):
        if var == "0" :
            self.update_done.configure(state="disabled")
        else:
            self.update_done.configure(state="active")
            
     #delete the selected contact       
    def delete_check(self,num):
        ans = askyesno("CONTACT BOOk","Are you sure you want to delete this contact?")
        if ans:
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("Delete from Contact_List where number = '{}';".format(num))
            con.commit()
            con.close()
            messagebox.showinfo("Message","Successfully Deleted.")
            self.open_contact_list()
            self.show_contact()
        else :
            self.open_delete_contact()
    
    #to search the contact whenever any character is entered on search bar.
    def search_contact(self,event):
        if self.search.get() == 'Search':
            self.search.delete(0,30)
        else:
            con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('select name,number from contact_list where name like "%{}%" or number like "%{}%";'.format(self.search.get(),self.search.get()))
            data=cur.fetchall()
            con.commit()
            con.close()
            if data != [] :
                self.contact_list.delete("1.0","10000.0")
                for i in data:
                    for j in i:
                        self.contact_list.insert(tk.INSERT,(j+'\n'))
            else:
                self.contact_list.delete("1.0","100.0")
                self.contact_list.insert("0.0","No Contact")
                
    # To get all the number present in database and show them on scrolled text.
    def show_contact(self):
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select name,number from contact_list;')
        data=cur.fetchall()
        con.commit()
        con.close()
        if len(data) > 0:
            self.contact_list.delete("1.0","10.0")
            for i in data:
                for j in i:
                    self.contact_list.insert(tk.INSERT,(j+'\n'))

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
            messagebox.showinfo("Message","Successfully UPDATED.")
            self.open_contact_list()
            self.show_contact()
        except:
            messagebox.showerror("Error","Invalid Phone Number")

    #Update Frame - to select the contact for updation.
    def open_update_contact(self):
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select name,number from contact_list;')
        data=cur.fetchall()
        con.commit()
        con.close()

        i = 0 #to change checkbutton id
        Y = 30 #to change checkbutton place
        var = tk.StringVar()    #to store contact number when checkbutton is checked

        
        self.checkbox_id = "checkbox"+str(i)        #Variable to store the id of checkbutton.
        self.update_contact = tk.Frame(self.contact_book)
        self.update_contact.configure(
            background="#000000", height=200, width=200)

        
        #it will create the number of checkbutton as equals to contact present in database.
        #Id of the checkbutton will be decided by self.checkbox_id
        while i < len(data):
            self.checkbox_id = tk.Checkbutton(self.update_contact)
            self.checkbox_id.configure(
                background="#000000",
                font="{Calibri} 14 {}",
                foreground="#787878",
                anchor="w",
                justify="left",
                variable=var,
                onvalue=data[i][1],
                offvalue=0,
                text=data[i][0]+" ("+data[i][1]+")",
                command=lambda:self.update_check(var.get()))
            self.checkbox_id.deselect()
            self.checkbox_id.place(
                height=30,
                width=200,
                x=0,
                y=Y)
            i += 1
            Y += 30

        self.back = tk.Button(self.update_contact)     #go back to home tab.
        self.back.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='←',
            command = self.open_contact_list)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
            
        self.update_done = tk.Button(self.update_contact) #To make changes in selected contact list for updation.
        self.update_done.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri Light} 20 {}",
            foreground="#ffffff",
            state="disabled",
            text='✓',
            command=lambda:self.update_contact_details(var.get()))
        self.update_done.place(anchor="nw", height=30, width=30, x=220, y=0)
        
        self.update_contact.place(anchor="nw", height=550, width=250, x=0, y=0)

    
    #getting full details of contact which is selected for updation
    def update_contact_details(self,var):
        
        #fetching from database
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select * from contact_list where number = "{}";'.format(var))
        data=cur.fetchall()
        con.commit()
        con.close()
        
        self.update_contact = tk.Frame(self.contact_book)
        self.update_contact.configure(background="#000000", height=200, width=200)
        
        label14 = tk.Label(self.update_contact)
        label14.configure(
            background="#000000",
            font="{Arial} 12 {}",
            foreground="#ffffff",
            text='UPDATE CONTACT')
        label14.place(anchor="nw", height=25, width=150, x=45, y=0)
        separator19 = ttk.Separator(self.update_contact)
        separator19.configure(orient="horizontal")
        separator19.place(anchor="nw", width=150, x=45, y=25)
        
        self.name = tk.Entry(self.update_contact)   #Update Name
        self.name.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.name.insert("0",data[0][0])
        self.name.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=80)
        
        self.number = tk.Entry(self.update_contact) #Update Number
        self.number.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.number.insert("0",data[0][1])
        self.number.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=145)
        
        self.email = tk.Entry(self.update_contact)      #Update Email
        self.email.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.email.insert("0",data[0][2])
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=210)

        self.landmark = tk.Entry(self.update_contact)       #Update landmark
        self.landmark.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.landmark.insert("0",data[0][3])
        self.landmark.place(anchor="nw", height=25, width=249, x=0, y=275)
        
        self.city = tk.Entry(self.update_contact)       #Update city
        self.city.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.city.insert("0",data[0][4])
        self.city.place(anchor="nw", height=25, width=249, x=0, y=340)
    
        self.state = tk.Entry(self.update_contact)      #Update State
        self.state.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.state.insert("0",data[0][5])
        self.state.place(anchor="nw", height=25, width=249, x=0, y=405)
        
        separator20 = ttk.Separator(self.update_contact)
        separator20.configure(orient="horizontal")
        separator20.place(anchor="nw", width=250, x=0, y=105)
        separator21 = ttk.Separator(self.update_contact)
        separator21.configure(orient="horizontal")
        separator21.place(anchor="nw", width=250, x=0, y=170)
        separator22 = ttk.Separator(self.update_contact)
        separator22.configure(orient="horizontal")
        separator22.place(anchor="nw", width=250, x=0, y=235)
        separator23 = ttk.Separator(self.update_contact)
        separator23.configure(orient="horizontal")
        separator23.place(anchor="nw", width=250, x=0, y=300)
        separator24 = ttk.Separator(self.update_contact)
        separator24.configure(orient="horizontal")
        separator24.place(anchor="nw", width=250, x=0, y=365)
        separator25 = ttk.Separator(self.update_contact)
        separator25.configure(orient="horizontal")
        separator25.place(anchor="nw", width=250, x=0, y=430)
        
        self.back = tk.Button(self.update_contact)      #go back 
        self.back.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='←',
            command = self.open_update_contact)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
        
        self.done = tk.Button(self.update_contact)  #Update done
        self.done.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri Light} 20 {}",
            foreground="#ffffff",
            text='✓',
            command=lambda:self.contact_updated(var))
        
        self.done.place(anchor="nw", height=30, width=30, x=220, y=0)
        self.update_contact.place(anchor="nw", height=550, width=250, x=0, y=0)
    
    #to select and delete the contact which no longer required.
    def open_delete_contact(self):
        
        con=ms.connect(host="localhost",database="ContactBook",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select name,number from contact_list;')
        data=cur.fetchall()
        con.commit()
        con.close()
        
        i = 0
        Y = 30
        self.l = []
        var = tk.StringVar()
        self.checkbox_id = "checkbox"+str(i)
        
        self.delete_contact = tk.Frame(self.contact_book)
        self.delete_contact.configure(
            background="#000000", height=200, width=200)
        
        while i < len(data):
            self.checkbox_id = tk.Checkbutton(self.delete_contact)
            self.checkbox_id.configure(
                background="#000000",
                font="{Calibri} 14 {}",
                foreground="#787878",
                anchor="w",
                justify="left",
                variable=var,
                state="normal",
                onvalue=data[i][1],
                offvalue=0,
                text=data[i][0]+" ("+data[i][1]+")",
                command=lambda:self.delete_check(var.get()))
            self.checkbox_id.deselect()
            self.checkbox_id.place(
                height=30,
                width=200,
                x=0,
                y=Y)
            i += 1
            Y += 30

        self.back = tk.Button(self.delete_contact)      #go back 
        self.back.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='←',
            command = self.open_contact_list)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
        
        self.delete_contact.place(anchor="nw", height=550, width=250, x=0, y=0)
    

    #This is " Contact list frame / Home frame " where list of all contact is shown or "No Contact" in case of empty contact list. 
    def open_contact_list(self):
        self.view_contact_list = tk.Frame(self.contact_book)
        self.view_contact_list.configure(
            background="#000000", height=200, width=200)
        
        self.search = tk.Entry(self.view_contact_list)  #Search Bar - for searching contact by name or number
        self.search.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        _text_ = 'Search'
        self.search.insert("0", _text_)
        self.search.place(anchor="nw", height=30, width=250, x=0, y=0)
        self.search.bind("<Button>",self.search_contact)
        self.search.bind("<KeyRelease>",self.search_contact)
        
        self.contact_list = ScrolledText(self.view_contact_list)    #Scrolled Text - "AlL contact are listed here"
        self.contact_list.configure(
            background="#000000",
            font="{Arial} 14 {}",
            foreground="#ffffff")
        _text_ = 'No Contact'
        self.contact_list.insert("0.0", _text_)
        self.contact_list.place(anchor="nw", height=485, width=250, x=0, y=30)
        
        self.add = tk.Button(self.view_contact_list) #Add button - to open add contact frame.
        self.add.configure(
            background="#787878",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='ADD',
            command=self.open_add_contact)
        self.add.place(anchor="nw", height=35, width=83, x=0, y=515)
        
        self.update = tk.Button(self.view_contact_list) #update button - to select the contact for updation.
        self.update.configure(
            background="#787878",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='UPDATE',
            command=self.open_update_contact)
        self.update.place(anchor="nw", height=35, width=84, x=83, y=515)
        
        self.delete = tk.Button(self.view_contact_list) #delete button - to select the contact for deletion.
        self.delete.configure(
            background="#787878",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='DELETE',
            command=self.open_delete_contact)
        self.delete.place(anchor="nw", height=35, width=83, x=167, y=515)
        
        separator26 = ttk.Separator(self.view_contact_list) #seperator for design purpose.
        separator26.configure(orient="horizontal")
        separator26.place(anchor="nw", width=250, x=0, y=30)
        self.view_contact_list.place(
            anchor="nw", height=550, width=250, x=0, y=0)
        
        self.show_contact() #this function is called to show all the contact present in database on scrolled text.

    #to add contact in the database.    
    def open_add_contact(self):
        self.add_contact = tk.Frame(self.contact_book)
        self.add_contact.configure(background="#000000", height=200, width=200)
        
        label14 = tk.Label(self.add_contact)
        label14.configure(
            background="#000000",
            font="{Arial} 12 {}",
            foreground="#ffffff",
            text='ADD CONTACT')
        label14.place(anchor="nw", height=25, width=120, x=65, y=0)
        
        separator19 = ttk.Separator(self.add_contact)
        separator19.configure(orient="horizontal")
        separator19.place(anchor="nw", width=120, x=65, y=25)
        
        self.name = tk.Entry(self.add_contact) #Enter Name
        self.name.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.name.insert("0",'NAME')
        self.name.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=80)
        self.name.bind('<Button>',self.clear)
        
        self.number = tk.Entry(self.add_contact)    #Enter Number
        self.number.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.number.insert("0",'Phone Number')
        self.number.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=145)
        self.number.bind('<Button>',self.clear1)
        
        self.email = tk.Entry(self.add_contact)     #Enter Email
        self.email.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.email.insert("0",'Email')
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=25,
            width=249,
            x=0,
            y=210)
        self.email.bind('<Button>',self.clear2)
        
        self.landmark = tk.Entry(self.add_contact)      #Enter Landmark
        self.landmark.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.landmark.insert("0",'Landmark')
        self.landmark.place(anchor="nw", height=25, width=249, x=0, y=275)
        self.landmark.bind('<Button>',self.clear3)
        
        self.city = tk.Entry(self.add_contact)  #Enter City
        self.city.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.city.insert("0",'City')
        self.city.place(anchor="nw", height=25, width=249, x=0, y=340)
        self.city.bind('<Button>',self.clear4)
        
        self.state = tk.Entry(self.add_contact)     #Enter State
        self.state.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 14 {}",
            foreground="#787878")
        self.state.insert("0",'State')
        self.state.place(anchor="nw", height=25, width=249, x=0, y=405)
        self.state.bind('<Button>',self.clear5)
        
        separator20 = ttk.Separator(self.add_contact)           #for design
        separator20.configure(orient="horizontal")
        separator20.place(anchor="nw", width=250, x=0, y=105)
        separator21 = ttk.Separator(self.add_contact)
        separator21.configure(orient="horizontal")
        separator21.place(anchor="nw", width=250, x=0, y=170)
        separator22 = ttk.Separator(self.add_contact)
        separator22.configure(orient="horizontal")
        separator22.place(anchor="nw", width=250, x=0, y=235)
        separator23 = ttk.Separator(self.add_contact)
        separator23.configure(orient="horizontal")
        separator23.place(anchor="nw", width=250, x=0, y=300)
        separator24 = ttk.Separator(self.add_contact)
        separator24.configure(orient="horizontal")
        separator24.place(anchor="nw", width=250, x=0, y=365)
        separator25 = ttk.Separator(self.add_contact)
        separator25.configure(orient="horizontal")
        separator25.place(anchor="nw", width=250, x=0, y=430)
        
        self.back = tk.Button(self.add_contact)     #go back to home tab.
        self.back.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='←',
            command = self.open_contact_list)
        self.back.place(anchor="nw", height=30, width=30, x=0, y=0)
        
        self.done = tk.Button(self.add_contact)     #add button - to add contact in database.
        self.done.configure(
            background="#000000",
            borderwidth=0,
            font="{Calibri Light} 20 {}",
            foreground="#ffffff",
            text='✓',
            command = self.contact_added)
        self.done.place(anchor="nw", height=30, width=30, x=220, y=0)
        
        self.add_contact.place(anchor="nw", height=550, width=250, x=0, y=0)

        
    def __init__(self, master=None):
        #build ui
        
        self.contact_book = tk.Tk() if master is None else tk.Toplevel(master)
        self.contact_book.configure(height=550, width=250)
        self.contact_book.resizable(False, False)
        self.contact_book.title("Contact Book")
        self.open_contact_list()    #Home tab
        self.show_contact()     #List of All Contact
        
        # Main widget
        self.mainwindow = self.contact_book

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = ContactBookApp()
    app.run()
