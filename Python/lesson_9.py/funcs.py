from PIL import ImageTk

def img_size(sc1, sc2, var, canvas, variant, imgs):
    w = sc2.get()
    h = sc1.get()
    a = var.get()
    if a in variant:
        orig_img = imgs[a]
        resized_mg = orig_img.resize((w, h))
        img_tk = ImageTk.PhotoImage(resized_mg)
        canvas.image = img_tk
        canvas.delete("all")
        canvas.create_image(0,0, anchor = "nw", image=img_tk)

def choice(sc1, sc2, var, canvas, variant, imgs):
    a = var.get()
    canvas.create_image(0, 0, anchor="nw", image=variant[a])
    img_size(sc1, sc2, var, canvas, variant, imgs)

def canvas_size(sc1, sc2, var, canvas, variant, imgs):
    w = sc2.get()
    h = sc1.get()
    canvas.config(width=w, height=h)
    img_size(sc1, sc2, var, canvas, variant, imgs)
