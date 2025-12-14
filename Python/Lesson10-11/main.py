from tkinter import *
import funcs

root = Tk()
width = 700
heidht = 400
root.title("Викторина")
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_heidht = root.winfo_screenheight()

x_offset = (screen_width - width) // 2
y_offset = (screen_heidht - heidht) // 2

root.geometry(f"{width}x{heidht}+{x_offset}+{y_offset}")

QUEST = Label(text="", font=("Arial", 16))
QUEST.place(anchor="center", relx=0.5, rely=0.15)

info = Label(text="", font=("Arial", 12), fg="red")
info.place(anchor="center", relx=0.5, rely=0.25)

buttons = []

for i in range(1, 5):
    btn = Button(width=50, height=1, font=("Arial", 14))
    btn.config(command=lambda b=btn: funcs.choice(b, QUEST, buttons, info))
    btn.place(anchor="center", relx=0.5, rely=0.25+0.15*i)
    buttons.append(btn)

funcs.genarate_quest(QUEST, buttons)











root.mainloop()