from tkinter import* 
from tkinter import messagebox

class App:
    def __init__(self):
        self.__window = Tk()
        self.__wight_window = 400
        self.__height_window = 500
        self.__screen_wight = self.__window.winfo_screenwidth()
        self.__screen_height = self.__window.winfo_screenheight()
        self.__x = (self.__screen_wight // 2) - (self.__wight_window // 2)
        self.__y = (self.__screen_height // 2) - (self.__height_window // 2)
        self._name_app = "Фипи банк 2.0"

    def clear_form(self):
        for widget in self.__window.winfo_children():
            widget.destroy()


    def start_form(self):
        self.clear_form()
        authorization_but = Button(self.__window, text="Авторизация", width=20, font=("Arial", 16))
        authorization_but.place(anchor="center", relx=0.5, rely=0.3)

        registration_but = Button(self.__window, text="Регистрация", width=20, font=("Arial", 16), command=self.registration_form)
        registration_but.place(anchor="center", relx=0.5, rely=0.4)

    def registration_form(self):
        self.clear_form()
        
        name_label = Label(self.__window, text="Имя пользователя", font=("Arial", 16))
        name_label.place(anchor="center", relx=0.5, rely=0.05)
        name = Entry(self.__window, width=20, font=("Arial", 16))
        name.place(anchor="center", relx=0.5, rely=0.15)

        
        phone_label = Label(self.__window, text="Номер телефона", font=("Arial", 16))
        phone_label.place(anchor="center", relx=0.5, rely=0.25)
        phone = Entry(self.__window, width=20, font=("Arial", 16))
        phone.place(anchor="center", relx=0.5, rely=0.35)


        password_label = Label(self.__window, text="Пароль", font=("Arial", 16))
        password_label.place(anchor="center", relx=0.5, rely=0.45)
        password = Entry(self.__window, width=20, font=("Arial", 16))
        password.place(anchor="center", relx=0.5, rely=0.55)

        repeat_password_label = Label(self.__window, text="Пароль", font=("Arial", 16))
        repeat_password_label.place(anchor="center", relx=0.5, rely=0.65)
        repeat_password = Entry(self.__window, width=20, font=("Arial", 16))
        repeat_password.place(anchor="center", relx=0.5, rely=0.75)

        registration_complite = Button(self.__window, text="Регистариция", width=15, font=("Arial", 16))
        registration_complite.place(anchor="center", relx= 0.5, rely= 0.90)


    def start(self):
        self.__window.geometry(f"{self.__wight_window}x{self.__height_window}+{self.__x}+{self.__y}")
        self.__window.resizable(False, False)
        self.__window.title(self._name_app)

        self.start_form()
        self.__window.mainloop()

    def valid_info(self, name, phone, password, repeat_password):

        if len(name) == 0 or len(phone) == 0 or len(password) == 0 or len(repeat_password) == 0:
            message_title = "Ошибка валидации"
            message_info = "Одно или несколько полей не заполнены!1"
            messagebox.showinfo(message_title, message_info)

        elif not name.isalpha():
            message_title = "Ошибка валидации"
            message_info = "Имя должно состоять только из буквенных символов!1"
            messagebox.showinfo(message_title, message_info)

        elif not phone.isdigit():
            message_title = "Ошибка валидации"
            message_info = "Номер должен состоять только из цифр!1"
            messagebox.showinfo(message_title, message_info)

        elif password != repeat_password():
            message_title = "Ошибка валидации"
            message_info = "Пароли не совпадают!1"
            messagebox.showinfo(message_title, message_info)






