#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
class CalculaterApp:
        
        def calculate(self):
            try:
                if '=' in self.value:
                    self.value=self.value[self.value.index('=')+1:]
                self.value=str(eval(self.value))
                self.display.configure(text=self.value)
            except:
                self.display.configure(text="Error")
        def show(self,v):
            if v == '0' and len(self.value) == 0 :
                pass
            elif v == '0' and len(self.value) != 0 :
                    if self.value[-1] == "+" or self.value[-1] == "-" or self.value[-1] == "/" or self.value[-1] == "*" or self.value[-1] == "(" or self.value[-1] == ")" :
                        pass
                    else :
                        if len(self.value) >= 18 :
                                self.value+=v
                                self.display.configure(font="{Times New Roman} 14 {bold}",
                                                       text=self.value)
                        elif len(self.value) < 18  :
                                self.value+=v
                                self.display.configure(font="{Times New Roman} 20 {bold}",
                                                       text=self.value)
            else :
                    if len(self.value) >= 18 :
                                self.value+=v
                                self.display.configure(font="{Times New Roman} 14 {bold}",
                                                       text=self.value)
                    elif len(self.value) < 18  :
                                self.value+=v
                                self.display.configure(font="{Times New Roman} 20 {bold}",
                                                       text=self.value)
                
        def clr(self):
            self.value=''
            self.display.configure(text=self.value)
        def dele(self):
            self.value=self.value[:-1]
            self.display.configure(text=self.value)
        
            
        def __init__(self, master=None):
            # build ui
            self.main_frame = tk.Tk() if master is None else tk.Toplevel(master)
            self.main_frame.configure(background="#000000", height=430, width=290)
            self.main_frame.title("Calculator")
            self.main_frame.resizable(False, False)
            self.display = tk.Label(self.main_frame)
            self.display.configure(
                font="{Times New Roman} 20 {bold}",
                foreground="#ffffff",
                background="#404040",
                anchor="e")
            self.display.place(anchor="nw", height=60, width=270, x=10, y=10)
            self.seven = tk.Button(self.main_frame)
            self.seven.configure(text='7',
                                 font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                 command=lambda:self.show("7"))
            self.seven.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=10,
                y=80)
            self.eight = tk.Button(self.main_frame)
            self.eight.configure(text='8',
                                 font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                 command=lambda:self.show("8"))
            self.eight.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=80,
                y=80)
            self.nine = tk.Button(self.main_frame)
            self.nine.configure(text='9',
                                font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                command=lambda:self.show("9"))
            self.nine.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=150,
                y=80)
            self.div = tk.Button(self.main_frame)
            self.div.configure(text="÷",
                               font="{Times New Roman} 35 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                               command=lambda:self.show("/"))
            self.div.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=220,
                y=80)
            self.four = tk.Button(self.main_frame)
            self.four.configure(text='4',
                                font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                command=lambda:self.show("4"))
            self.four.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=10,
                y=150)
            self.five = tk.Button(self.main_frame)
            self.five.configure(text='5',
                                font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                command=lambda:self.show("5"))
            self.five.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=80,
                y=150)
            self.six = tk.Button(self.main_frame)
            self.six.configure(text='6',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                               command=lambda:self.show("6"))
            self.six.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=150,
                y=150)
            self.mul = tk.Button(self.main_frame)
            self.mul.configure(text='×',
                               font="{Times New Roman} 30 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                               command=lambda:self.show("*"))
            self.mul.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=220,
                y=150)
            self.one = tk.Button(self.main_frame)
            self.one.configure(text='1',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                               command=lambda:self.show("1"))
            self.one.place(
                anchor="nw",
                bordermode="outside",
                height=60,
                relheight=0.0,
                width=60,
                x=10,
                y=220)
            self.two = tk.Button(self.main_frame)
            self.two.configure(text='2',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                               command=lambda:self.show("2"))
            self.two.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=80,
                y=220)
            self.three = tk.Button(self.main_frame)
            self.three.configure(text='3',
                                 font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                 command=lambda:self.show("3"))
            self.three.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=150,
                y=220)
            self.sub = tk.Button(self.main_frame)
            self.sub.configure(text='−',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                               command=lambda:self.show("-"))
            self.sub.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=220,
                y=220)
            self.zero = tk.Button(self.main_frame)
            self.zero.configure(text='0',
                                font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                command=lambda:self.show("0"))
            self.zero.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=10,
                y=290)
            self.point = tk.Button(self.main_frame)
            self.point.configure(text='.',
                                 font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                                 command=lambda:self.show("."))
            self.point.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=150,
                y=360)
            self.equ = tk.Button(self.main_frame)
            self.equ.configure(text='=',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                               command=self.calculate)
            self.equ.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=220,
                y=360)
            self.add = tk.Button(self.main_frame)
            self.add.configure(text='+',
                               font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#00ce34",
                               command=lambda:self.show("+"))
            self.add.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=220,
                y=290)
            self.clear = tk.Button(self.main_frame)
            self.clear.configure(text='AC',
                                 font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#eb0214",
                                 command=self.clr)
            self.clear.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=10,
                y=360)
            self.delete = tk.Button(self.main_frame)
            self.delete.configure(text='C',
                                  font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#eb0214",
                                  command=self.dele)
            self.delete.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=80,
                y=360)
            self.left_p = tk.Button(self.main_frame)
            self.left_p.configure(text='(',
                                  font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                  command=lambda:self.show("("))
            self.left_p.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=80,
                y=290)
            self.right_p = tk.Button(self.main_frame)
            self.right_p.configure(text=')',
                                   font="{Times New Roman} 25 {bold}",
                                 foreground="#ffffff",
                                 background="#404040",
                                   command=lambda:self.show(")"))
            self.right_p.place(
                anchor="nw",
                bordermode="ignore",
                height=60,
                relheight=0.0,
                width=60,
                x=150,
                y=290)
            
            self.value=''

            # Main widget
            self.mainwindow = self.main_frame

        def run(self):
            self.mainwindow.mainloop()


if __name__ == "__main__":
        app = CalculaterApp()
        app.run()

    
