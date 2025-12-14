from tkinter import *
from PIL import ImageTk, Image
from funcs import choice, canvas_size

root = Tk()
root.title("Котики")
root.geometry('800x720')
root.resizable(width=False, height=False)

imgs = {1: Image.open('lesson_9.py\images\cat1.jpg'),
        2: Image.open('lesson_9.py\images\cat2.jpg'),
        3: Image.open('lesson_9.py\images\cat3.jpg'),
        4: Image.open('lesson_9.py\images\cat4.jpg')}


img_b1 = imgs[1].resize((150, 150))
img_b1 = ImageTk.PhotoImage(img_b1)

img_b2 = imgs[2].resize((150, 150))
img_b2 = ImageTk.PhotoImage(img_b2)

img_b3 = imgs[3].resize((150, 150))
img_b3 = ImageTk.PhotoImage(img_b3)

img_b4 = imgs[4].resize((150, 150))
img_b4 = ImageTk.PhotoImage(img_b4)

variant = {1: img_b1,
           2: img_b2,
           3: img_b3,
           4: img_b4}

var = IntVar()
var.set(0)

b1 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b1, 
                 command=lambda: choice(sc1, sc2, var, canvas, variant, imgs))
b1.place(relx=0.1, rely=0.75)

b2 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b2, 
                 command=lambda: choice(sc1, sc2, var, canvas, variant, imgs))
b2.place(relx=0.3, rely=0.75)

b3 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b3,
                 command=lambda: choice(sc1, sc2, var, canvas, variant, imgs))
b3.place(relx=0.5, rely=0.75)

b4 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b4,
                 command=lambda: choice(sc1, sc2, var, canvas, variant, imgs))
b4.place(relx=0.7, rely=0.75)

sc1 = Scale(from_=50, to=400, length=400,
            command=lambda val: canvas_size(sc1, sc2, var, canvas, variant, imgs))
sc1.place(relx=0.18, rely=0.1)

sc2 = Scale(from_=50, to=400, length=400, orient='horizontal',
            command=lambda val: canvas_size(sc1, sc2, var, canvas, variant, imgs))
sc2.place(relx=0.25, rely=0.03)

canvas = Canvas(width=50, height=50, bg="white")
canvas.place(relx=0.25, rely=0.1)


root.mainloop()