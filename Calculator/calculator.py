#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
        value=''
        def calculate(self):
            try:
                if '=' in self.value:
                    self.value=self.value[self.value.index('=')+1:]
                self.value=str(eval(self.value))
                self.display.configure(text=self.value)
            except:
                self.display.configure(text="Error")
        def show(self,v):
            self.value+=v
            self.display.configure(text=self.value)
        def clr(self):
            self.value=''
            self.display.configure(text=self.value)
        def dele(self):
            self.value=self.value[:-1]
            self.display.configure(text=self.value)
        
            
        def __init__(self, master=None):
            # build ui
            self.main_frame = tk.Tk() if master is None else tk.Toplevel(master)
            self.main_frame.configure(background="#000000", height=350, width=235)
            self.main_frame.title("calculator")
            self.main_frame.resizable(False, False)
            self.display = ttk.Label(self.main_frame)
            self.display.configure(
                font="{Times New Roman} 16 {bold}",
                justify="left")
            self.display.place(anchor="nw", height=49, width=244, x=0, y=0)
            self.seven = ttk.Button(self.main_frame)
            self.seven.configure(text='7',command=lambda:self.show("7"))
            self.seven.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=0,
                y=51)
            self.eight = ttk.Button(self.main_frame)
            self.eight.configure(text='8',command=lambda:self.show("8"))
            self.eight.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=61,
                y=51)
            self.nine = ttk.Button(self.main_frame)
            self.nine.configure(text='9',command=lambda:self.show("9"))
            self.nine.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=122,
                y=51)
            self.div = ttk.Button(self.main_frame)
            self.div.configure(text='/',command=lambda:self.show("/"))
            self.div.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=184,
                y=51)
            self.four = ttk.Button(self.main_frame)
            self.four.configure(text='4',command=lambda:self.show("4"))
            self.four.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=0,
                y=111)
            self.five = ttk.Button(self.main_frame)
            self.five.configure(text='5',command=lambda:self.show("5"))
            self.five.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=61,
                y=111)
            self.six = ttk.Button(self.main_frame)
            self.six.configure(text='6',command=lambda:self.show("6"))
            self.six.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=122,
                y=111)
            self.mul = ttk.Button(self.main_frame)
            self.mul.configure(text='X',command=lambda:self.show("*"))
            self.mul.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=184,
                y=111)
            self.one = ttk.Button(self.main_frame)
            self.one.configure(text='1',command=lambda:self.show("1"))
            self.one.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=0,
                y=172)
            self.two = ttk.Button(self.main_frame)
            self.two.configure(text='2',command=lambda:self.show("2"))
            self.two.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=61,
                y=172)
            self.three = ttk.Button(self.main_frame)
            self.three.configure(text='3',command=lambda:self.show("3"))
            self.three.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=122,
                y=172)
            self.sub = ttk.Button(self.main_frame)
            self.sub.configure(text='-',command=lambda:self.show("-"))
            self.sub.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=184,
                y=172)
            self.zero = ttk.Button(self.main_frame)
            self.zero.configure(text='0',command=lambda:self.show("0"))
            self.zero.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=0,
                y=233)
            self.point = ttk.Button(self.main_frame)
            self.point.configure(text='.',command=lambda:self.show("."))
            self.point.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=61,
                y=233)
            self.equ = ttk.Button(self.main_frame)
            self.equ.configure(text='=',command=self.calculate)
            self.equ.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=122,
                y=233)
            self.add = ttk.Button(self.main_frame)
            self.add.configure(text='+',command=lambda:self.show("+"))
            self.add.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=184,
                y=233)
            self.clear = ttk.Button(self.main_frame)
            self.clear.configure(text='c',command=self.clr)
            self.clear.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=0,
                y=294)
            self.delete = ttk.Button(self.main_frame)
            self.delete.configure(text='Del',command=self.dele)
            self.delete.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=61,
                y=294)
            self.left_p = ttk.Button(self.main_frame)
            self.left_p.configure(text='(',command=lambda:self.show("("))
            self.left_p.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=122,
                y=294)
            self.right_p = ttk.Button(self.main_frame)
            self.right_p.configure(text=')',command=lambda:self.show(")"))
            self.right_p.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=184,
                y=294)

            # Main widget
            self.mainwindow = self.main_frame

        def run(self):
            self.mainwindow.mainloop()


if __name__ == "__main__":
        app = NewprojectApp()
        app.run()

    
