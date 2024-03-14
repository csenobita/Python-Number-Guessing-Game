from tkinter import *
from random import randint
from tkinter import messagebox
import time

class guress_number:
    def __init__(self, root):
        self.root = root
        self.fbg = '#658ddd'

        self.font = ("Arial", 30, 'bold')
        self.font1 = ("Arial", 15, 'bold')

        self.root.title("Guress Number")
        self.root.geometry("1000x800+400+100")
        self.root.resizable(False, False)

        self.score_var = StringVar()
        self.number_var = StringVar()
        self.score_var.set(10)

        self.fream1 = Frame(self.root, width=1000, height=800, bd=12, bg=self.fbg)
        self.fream1.pack()

        self.title_label = Label(self.fream1, text='Guress Number Game', font=self.font,
                                 bg=self.fbg)
        self.title_label.place(x=250, y=30)

        self.title_label2 = Label(self.fream1, text='I Challenge to you guress the number (0 to 50) : ',
                                  font=self.font1,
                                  bg=self.fbg)
        self.title_label2.place(x=80, y=250)

        self.number_box = Entry(self.fream1, font=self.font1, width=4, justify='center', bd=0, relief=RIDGE,
                                textvariable=self.number_var)
        self.number_box.place(x=550, y=250)

        self.button_box = Button(self.fream1, text='Guess', font=self.font1, bg='green', bd=0, relief=RIDGE,
                                 cursor='hand2', command=self.button_click)
        self.button_box.place(x=750, y=250)

        self.text_box = Entry(self.fream1, font=self.font1, bg=self.fbg, width=50, bd=0, relief=RIDGE, justify='center',
                              fg='black')
        self.text_box.place(x=200, y=400)

        self.score_label = Label(self.fream1, text='Your score 10 out of : ', width=20, height=1, font=self.font1,
                                 bg=self.fbg)
        self.score_label.place(x=280, y=500)
        self.score_entry = Entry(self.fream1, font=self.font1, width=3, justify='center', bd=0, relief=RIDGE,
                                 textvariable=self.score_var,state=DISABLED,fg='black')
        self.score_entry.place(x=550, y=500)

    def button_click(self):
        num = randint(0, 50)
        if 51 > int(self.number_var.get()):
            if int(self.score_var.get())>0:
                if num == int(self.number_var.get()):
                    self.text_box.delete(0, END)
                    self.story = "You are guress number game win. 🥰🥰🥰"
                    self.text_box.insert(END, self.story)
                    self.text_box.config(self.fbg)
                    time.sleep(10)

                elif num < int(self.number_var.get()):
                    score=int(self.score_var.get())
                    self.score_var.set(score-1)
                    self.text_box.delete(0, END)
                    self.story = "You are guress number Big. Try aging 😑"
                    self.text_box.insert(END, self.story)
                    self.text_box.config(bg=self.fbg)

                elif num > int(self.number_var.get()):

                    score=int(self.score_var.get())
                    self.score_var.set(score-1)
                    self.text_box.delete(0, END)
                    self.story = "You are guress number smaller . Try aging 😉"
                    self.text_box.insert(END, self.story)
                    self.text_box.config(bg=self.fbg)
            else:
                messagebox.showwarning('Error', 'Your are loss the game Please try aging')
                self.score_var.set(10)



        else:
            messagebox.showinfo('Error', 'Please enter a number between 0 to 50')


if __name__ == '__main__':
    root = Tk()
    app = guress_number(root)
    root.mainloop()
