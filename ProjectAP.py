import tkinter as tk
from tkinter import font
from tkinter import Frame
from PIL import ImageTk, Image

font_name = "Nazanin"
font_size = 11
font_style = "bold"

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("کرفس")
        self.geometry("800x600")

        self.logo_image()
        self.create_search_field()
        self.create_category_buttons()
        self.create_login_button()
        
    def logo_image(self):
        image = Image.open("image/celery2.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=340, y=140)

    def create_search_field(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        label = tk.Label(self, text=" :نام محصول را وارد کنید", font=my_font)
        label.place(x=323, y=230)

        entry = tk.Entry(self)
        entry.place(x=330, y=260)

        button = tk.Button(self, text="جستجو", command=self.search_result, width=10)
        button.place(x=353, y=285)

    def create_category_buttons(self):
        button1 = tk.Button(self, text="دسته بندی اول", width=15, height= 2)
        button1.grid(row=0, column=0)
        button1.configure(bg='light gray')

        button2 = tk.Button(self, text="دسته بندی دوم", width=15, height= 2)
        button2.grid(row=0, column=1)
        button2.configure(bg='light gray')

        button3 = tk.Button(self, text="دسته بندی سوم", width=15, height= 2)
        button3.grid(row=0, column=2)
        button3.configure(bg='light gray')

        button4 = tk.Button(self, text="دسته بندی چهارم", width=15, height= 2)
        button4.grid(row=0, column=3)
        button4.configure(bg='light gray')

        button5 = tk.Button(self, text="دسته بندی پنجم", width=15, height= 2)
        button5.grid(row=0, column=4)
        button5.configure(bg='light gray')

    def create_login_page(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        label_username = tk.Label(self, text='نام کاربری:')
        label_username.place(x=295, y=260)
        entry_username = tk.Entry(self)
        entry_username.place(x=360, y=260)
        label_password = tk.Label(self, text='رمز عبور:')
        label_password.place(x=300, y=290)
        entry_password = tk.Entry(self, show='*')
        entry_password.place(x=360, y=290)
        button_save = tk.Button(self, text='ذخیره', command=self.save_data, width=10)
        button_save.place(x=380, y=320)
        label_status = tk.Label(self, text='')
        label_status.place(x=370, y=350)
        
        self.entry_username = entry_username
        self.entry_password = entry_password
        self.label_status = label_status
        
    def create_login_button(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        loginbutton = tk.Button(self, text="ورود / ثبت نام", width=10, height=2, font=my_font , command=self.open_new_page)
        loginbutton.place(x=660, y=0)
        loginbutton.configure(bg='light gray')

    def save_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
    
        with open('user_data.txt', 'a') as file:
            file.write(f'user: {username}\n')
            file.write(f'pass: {password}\n')
            file.write('----------\n')
    
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.label_status.config(text='! با موفقیت ثبت شد')

    def open_new_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        new_frame1 = Frame(self)
        new_frame1.pack()

        new_button1 = tk.Button(new_frame1, text="بازگشت به صفحه اصلی", command=self.return_to_main_page)
        new_button1.pack()
        
        self.create_login_page()

    def return_to_main_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.logo_image()
        self.create_search_field()
        self.create_category_buttons()
        self.create_login_button()

    def search_result(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        new_frame2 = Frame(self)
        new_frame2.pack()
        
        new_button2 = tk.Button(new_frame2, text="بازگشت به صفحه اصلی", command=self.return_to_main_page)
        new_button2.pack()
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()