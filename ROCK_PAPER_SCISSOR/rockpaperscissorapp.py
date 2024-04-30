#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class RockPaperScissorApp:
    def __init__(self, master=None):
        # build ui
        self.main_frame = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_frame.configure(background="#c0c0c0", height=500, width=300)
        self.main_frame.resizable(False, False)
        self.main_frame.title("ROCK PAPER SCISSOR")
        self.game_frame = tk.Frame(self.main_frame)
        self.game_frame.configure(background="#408080", height=500, width=300)
        label1 = tk.Label(self.game_frame)
        label1.configure(
            background="#408080",
            font="{Arial Black} 14 {}",
            foreground="#000000",
            text='ROCK_PAPER_SCISSOR')
        label1.place(anchor="nw", height=30, width=260, x=20, y=5)
        separator1 = ttk.Separator(self.game_frame)
        separator1.configure(orient="horizontal")
        separator1.place(
            anchor="nw",
            bordermode="outside",
            height=3,
            width=260,
            x=20,
            y=36)
        self.computer_move = ttk.Label(self.game_frame)
        self.img_com_resized = tk.PhotoImage(file="com_resized.png")
        self.computer_move.configure(
            background="#ffffff",
            image=self.img_com_resized)
        self.computer_move.place(
            anchor="nw", height=100, width=100, x=20, y=130)
        self.players_move = ttk.Label(self.game_frame)
        self.img_hum = tk.PhotoImage(file="hum.png")
        self.players_move.configure(background="#ffffff", image=self.img_hum)
        self.players_move.place(
            anchor="nw",
            height=100,
            width=100,
            x=180,
            y=130)
        self.label7 = ttk.Label(self.game_frame)
        self.label7.configure(
            background="#408080",
            font="{Arial Black} 16 {bold}",
            text='VS')
        self.label7.place(anchor="nw", height=35, width=35, x=134, y=160)
        self.result = ttk.Label(self.game_frame)
        self.result.configure(
            background="#408080",
            font="{Arial Black} 12 {bold}",
            foreground="#000000",
            justify="center",
            text='       WELCOME')
        self.result.place(anchor="nw", height=25, width=160, x=70, y=260)
        self.rock = tk.Button(self.game_frame)
        self.rock.configure(
            activebackground="#ffffff",
            background="#c0c0c0",
            font="{Segoe UI Black} 13 {}",
            text='ROCK')
        self.rock.place(anchor="nw", height=30, width=80, x=15, y=315)
        self.paper = tk.Button(self.game_frame)
        self.paper.configure(
            activebackground="#ffffff",
            background="#c0c0c0",
            font="{Segoe UI Black} 13 {}",
            text='PAPER')
        self.paper.place(anchor="nw", height=30, width=80, x=110, y=315)
        self.play_again = tk.Button(self.game_frame)
        self.play_again.configure(
            background="#15ff50",
            font="{Cooper Black} 16 {}",
            text='Play Again')
        self.play_again.place(anchor="nw", height=40, width=160, x=70, y=365)
        self.scissor = tk.Button(self.game_frame)
        self.scissor.configure(
            background="#c0c0c0",
            font="{Segoe UI Black} 13 {}",
            text='SCISSOR')
        self.scissor.place(anchor="nw", height=30, width=80, x=205, y=315)
        self.back = tk.Button(self.game_frame)
        self.back.configure(
            background="#d70428",
            font="{Cooper Black} 16 {}",
            text='BACK')
        self.back.place(anchor="nw", height=40, width=160, x=70, y=415)
        label2 = tk.Label(self.game_frame)
        label2.configure(
            background="#408080",
            font="{Arial Black} 14 {}",
            foreground="#000000",
            text='Computer')
        label2.place(anchor="nw", height=30, width=100, x=20, y=100)
        label3 = tk.Label(self.game_frame)
        label3.configure(
            background="#408080",
            font="{Arial Black} 14 {}",
            foreground="#000000",
            text='Player')
        label3.place(anchor="nw", height=30, width=100, x=180, y=100)
        self.computer_score = ttk.Label(self.game_frame)
        self.computer_score.configure(
            background="#408080",
            font="{Arial Black} 12 {bold}",
            justify="center",
            text='00')
        self.computer_score.place(
            anchor="nw", height=25, width=25, x=20, y=232)
        self.player_score = ttk.Label(self.game_frame)
        self.player_score.configure(
            background="#408080",
            font="{Arial Black} 12 {bold}",
            justify="center",
            text='00')
        self.player_score.place(anchor="nw", height=25, width=25, x=255, y=232)
        self.label6 = ttk.Label(self.game_frame)
        self.label6.configure(
            background="#408080",
            font="{Arial Black} 12 {bold}",
            foreground="#ffff00",
            justify="center",
            text='10 MOVES / ROUND')
        self.label6.place(anchor="nw", height=25, width=175, x=70, y=50)
        self.game_frame.place(anchor="nw", x=0, y=0)

        # Main widget
        self.mainwindow = self.main_frame

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = RockPaperScissorApp()
    app.run()
