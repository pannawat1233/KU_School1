import tkinter as tk
from tkinter import messagebox
import random
class MainWindow(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title("MainWindow")
        self.geometry("554x413")
        
        self.label1 = tk.Label(self, text="Player1")
        self.label1.place(x=20, y=80, width=71, height=61)

        self.label2 = tk.Label(self, text="Player2")
        self.label2.place(x=20, y=140, width=71, height=61)

        self.Card1P1_var = tk.IntVar()
        self.Card2P1_var = tk.IntVar()
        self.point1_var = tk.IntVar()
        self.Card1P2_var = tk.IntVar()
        self.Card2P2_var = tk.IntVar()
        self.point2_var = tk.IntVar()


        self.Card1P1 = tk.Entry(self, textvariable=self.Card1P1_var)
        self.Card1P1.place(x=110, y=100, width=113, height=20)

        self.Card2P1 = tk.Entry(self, textvariable=self.Card2P1_var)
        self.Card2P1.place(x=230, y=100, width=113, height=20)

        self.point1 = tk.Entry(self, textvariable=self.point1_var)
        self.point1.place(x=350, y=100, width=113, height=20)

        self.Card1P2 = tk.Entry(self, textvariable=self.Card1P2_var)
        self.Card1P2.place(x=110, y=160, width=113, height=20)

        self.Card2P2 = tk.Entry(self, textvariable=self.Card2P2_var)
        self.Card2P2.place(x=230, y=160, width=113, height=20)

        self.point2 = tk.Entry(self, textvariable=self.point2_var)
        self.point2.place(x=350, y=160, width=113, height=20)

        self.WL = tk.Entry(self)
        self.WL.place(x=110, y=210, width=113, height=20)

        self.label3 = tk.Label(self, text="Card1")
        self.label3.place(x=140, y=30, width=71, height=61)

        self.label4 = tk.Label(self, text="Card2")
        self.label4.place(x=250, y=30, width=71, height=61)

        self.label5 = tk.Label(self, text="Point")
        self.label5.place(x=370, y=30, width=71, height=61)

        self.Click = tk.Button(self, text="Click",command=self.number)
        self.Click.place(x=380, y=290, width=101, height=41)

    def number(self):
        try:   
           
            random_subject = random.randint(1,100)
            random_subject1 = random.randint(1,100)
            random_subject2 = random.randint(1,100)
            random_subject3 = random.randint(1,100)
            
            self.Card1P1_var.set(random_subject)
            self.Card1P2_var.set(random_subject1)
            self.Card2P1_var.set(random_subject2)
            self.Card2P2_var.set(random_subject3)
            self.point1_var.set((random_subject+random_subject1)%10)
            self.point2_var.set((random_subject2+random_subject3)%10)

            if self.point2_var.get() < self.point1_var.get():
                self.WL.delete(0, tk.END)
                self.WL.insert(0,"player 1ชนะ")
            elif self.point2_var.get() > self.point1_var.get():
                self.WL.delete(0, tk.END)
                self.WL.insert(0, "Player 2 ชนะ")
            else:
                self.WL.delete(0, tk.END)
                self.WL.insert(0, "เสมอกัน")

        except ValueError:
            messagebox.showinfo("กรุณาใส่ข้อมูลที่ถูกต้อง")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()