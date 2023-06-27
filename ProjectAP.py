import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import font
from tkinter import Frame
from PIL import ImageTk, Image
import os
import stat

font_name = "Nazanin"
font_size = 11
font_style = "bold"

class Application(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        self.title("کرفس")
        self.geometry("800x600")
        self.conn = sqlite3.connect("data.db")
        db_path = 'data.db'
        new_permissions = stat.S_IRUSR
        os.chmod(db_path, new_permissions)
        self.c = self.conn.cursor()
        self.data_table()
        self.search_box()
        self.category_buttons()
        self.login_button()
        self.signup_button()
        self.logo_image()

    def data_table(self):
            
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (name text , username text ,password text)""")
        self.conn.commit()

    def logo_image(self):
        
        image = Image.open("image/celery2.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=340, y=130)
        my_font = font.Font(size='18', weight=font_style)
        label = tk.Label(self, text="کرفس", font=my_font)
        label.place(x=365, y=110)

    def search_box(self):
        
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        label1 = tk.Label(self, text=" :نام محصول را وارد کنید", font=my_font)
        label1.place(x=323, y=230)

        self.entry = tk.Entry(self)
        self.entry.place(x=330, y=260)

        button = tk.Button(self, text="جستجو", command=self.search_result, width=10)
        button.place(x=353, y=290)
        
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        label2 = tk.Label(self, text=" مقایسه بین محصولات مختلف", font=my_font)
        label2.place(x=310, y=320)

    def category_buttons(self):
        
        button1 = tk.Button(self, text=" هدفون و هدست ", width=15, height=2)
        button1.grid(row=0, column=0)
        button1.configure(bg='light gray')

        button2 = tk.Button(self, text=" تلفن همراه ", width=15, height=2)
        button2.grid(row=0, column=1)
        button2.configure(bg='light gray')

        button3 = tk.Button(self, text=" لپتاپ ", width=15, height=2)
        button3.grid(row=0, column=2)
        button3.configure(bg='light gray')

        button4 = tk.Button(self, text=" دوربین عکاسی ", width=15, height=2)
        button4.grid(row=0, column=3)
        button4.configure(bg='light gray')

        button5 = tk.Button(self, text=" کنسول بازی ", width=15, height=2)
        button5.grid(row=0, column=4)
        button5.configure(bg='light gray')

    def login_button(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        loginbutton = tk.Button(self, text="ورود", width=7, height=2, font=my_font, command=self.login_page)
        loginbutton.place(x=620, y=0)
        loginbutton.configure(bg='light gray')

    def signup_button(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        signupbutton = tk.Button(self, text="ثبت نام", width=7, height=2, font=my_font, command=self.signup_page)
        signupbutton.place(x=700, y=0)
        signupbutton.configure(bg='light gray')

    def logout_button(self):
        my_font = font.Font(family=font_name, size=font_size, weight=font_style)
        loginbutton = tk.Button(self, text="خروج از حساب کاربری", width=15, height=2, font=my_font, command=self.logout)
        loginbutton.place(x=620, y=0)
        loginbutton.configure(bg='light gray')
    
    def login_page(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        new_frame = Frame(self)
        new_frame.pack()

        new_button = tk.Button(new_frame, text="بازگشت به صفحه اصلی", command=self.return_to_main_page, width=20 , height=2)
        new_button.pack()
            
        login_username_label = Label(self, text=": نام کاربری")
        login_username_label.place(x=450 , y=258)
        self.login_username_entry = Entry(self)
        self.login_username_entry.place(x=315 , y=260)

        login_password_label = Label(self, text=": رمز عبور")
        login_password_label.place(x=450 , y=288)
        self.login_password_entry = Entry(self, show="•")
        self.login_password_entry.place(x=315 , y=290)

        login_button = Button(self, text="ورود", width=10, command=self.login)
        login_button.place(x=335 , y=320)

    def signup_page(self):

        for widget in self.winfo_children():
            widget.destroy()
            
        new_frame = Frame(self)
        new_frame.pack()

        new_button = tk.Button(new_frame, text="بازگشت به صفحه اصلی", command=self.return_to_main_page, width=20 , height=2)
        new_button.pack()
            
        signup_name_label = Label(self, text=":نام و نام خانوادگی")
        signup_name_label.place(x=450 , y=238)
        self.signup_name_entry = Entry(self)
        self.signup_name_entry.place(x=315 , y=240)
            
        signup_username_label = Label(self, text=":نام کاربری")
        signup_username_label.place(x=450 , y=268)
        self.signup_username_entry = Entry(self)
        self.signup_username_entry.place(x=315 , y=270)

        signup_password_label = Label(self, text=":رمز عبور")
        signup_password_label.place(x=450 , y=298)
        self.signup_password_entry = Entry(self, show="•")
        self.signup_password_entry.place(x=315 , y=300)

        signup_button = Button(self, text="ثبت نام", width=10, command=self.signup)
        signup_button.place(x=335 , y=330)
        
        label_status = tk.Label(self, text='')
        label_status.place(x=300, y=370)
        self.label_status = label_status
        
    def login(self):
        
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        self.c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = self.c.fetchall()
        self.conn.commit()

        if result and username != '':
            messagebox.showinfo('ورود موفق', message= "! با موفقیت وارد شدید")
            self.loged_in()
        else :
            messagebox.showerror('ورود ناموفق', message= "! نام کاربری یا رمز عبور صحیح نیست")

    def signup(self):
        
        self.label_status.destroy()
        
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        name = self.signup_name_entry.get()

        self.c.execute("INSERT INTO users VALUES (? ,?, ?)", (name, username, password))
        self.conn.commit()

        self.signup_username_entry.delete(0, END)
        self.signup_password_entry.delete(0, END)
        self.signup_name_entry.delete(0, END)
        
        if username == '' or password == '':
            messagebox.showerror('ثبت نام ناموفق', message= "! اطلاعات وارد شده صحیح نیست")
        else :
            messagebox.showinfo('ثبت نام موفق', message= "! با موفقیت ثبت شد")
            
    def logout(self):
        answer = messagebox.askyesno(' خروج از حساب ', message= "از حساب کاربری خارج می شوید؟")
        if answer == YES:
            self.return_to_main_page()
        
    def return_to_main_page(self):
        
        for widget in self.winfo_children():
            widget.destroy()

        self.search_box()
        self.category_buttons()
        self.login_button()
        self.signup_button()
        self.logo_image()

    def loged_in (self):
        
        for widget in self.winfo_children():
            widget.destroy()
        self.search_box()
        self.category_buttons()
        self.logout_button()
        self.logo_image()
        
    def search_result(self):
        for widget in self.winfo_children():
            widget.destroy()

        new_frame = Frame(self)
        new_frame.pack()

        new_button = tk.Button(new_frame, text="بازگشت به صفحه اصلی", command=self.return_to_main_page, width=20 , height=2)
        new_button.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
