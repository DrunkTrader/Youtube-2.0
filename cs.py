import tkinter
from tkinter import*
from tkinter import messagebox
import mysql.connector as ms
from PIL import ImageTk,Image
import time
import datetime
import random

print()

h=2
w=300
db = ms.connect(host="localhost",user="root",password='1122',database='school_project')
cur = db.cursor()
screen1 = Tk()

def star():
    print('*'*157)
   
class HoverButton(tkinter.Button):
    def __init__(self, master, **kw):
        tkinter.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def quit_screen():
    msg=messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if(msg=='yes'):
        screen1.destroy()
        quit()


def studentlogin():
    canvas2.destroy()
    l2.destroy()
    def login_verify():
        cur.execute("select * from student")
        results=cur.fetchall()
        for row in results:
            if(username.get()==row[0]):
                if(password.get()==row[5]):
                    std_login()

                    
                else:
                    messagebox.showerror("","Invalid Password")
          
            else:
                messagebox.showerror("","Invalid User ID")
                 
                      
    def reset():
        username.set('')
        password.set('')

    frame=LabelFrame(screen1,width = 600 , height =400,bg='white').place(x=650,y=370)

    username = StringVar()
    password = StringVar()

    Label(frame,text = "Student Login Panel" , width = 15 , height = 1,
          font = ("times new roman", 30) ,anchor=N,
           fg = "deepskyblue4",bg='white').place(x=800,y=395)
    
    Label(frame, text = "User ID :",font = ("Calibri", 18),bg='white').place(x=700, y = 470)
    username_entry= Entry(frame, textvariable = username,
                            width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=520)
    Label(frame, text = "Ex: 20012345",font = ("Calibri", 14),bg='white').place(x=1100, y = 515)
   
    Label(frame, text="Password :",font = ("Calibri", 18),bg='white').place(x=700, y=570)   
    password_entry= Entry(frame, textvariable = password,
                          show="*",width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=615)
    Label(frame, text = "Ex: 21-OCT-2003",font = ("Calibri", 14),bg='white').place(x=1100, y = 610)
    
    login=HoverButton(frame,text = "Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=login_verify).place(x=750 , y=700)
    reset=HoverButton(frame,text = "Reset", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=reset).place(x=1000 , y=700)



def stafflogin():
    canvas2.destroy()
    l2.destroy()
    def login_verify():
        cur.execute("select * from staff")
        results=cur.fetchall()
        for row in results:
            if(username.get()==row[0]):
                if(password.get()==row[5]):
                    std_login()

                    
                else:
                    messagebox.showerror("","Invalid Password")
          
            else:
                messagebox.showerror("","Invalid User ID")
                 
                      
    def reset():
        username.set('')
        password.set('')

    frame=LabelFrame(screen1,width = 600 , height =400,bg='white').place(x=650,y=370)

    username = StringVar()
    password = StringVar()

    Label(frame,text = "Staff Login Panel" , width = 15 , height = 1,
          font = ("times new roman", 30) ,anchor=N,
           fg = "deepskyblue4",bg='white').place(x=800,y=395)
    
    Label(frame, text = "User ID :",font = ("Calibri", 18),bg='white').place(x=700, y = 470)
    username_entry= Entry(frame, textvariable = username,
                            width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=520)
    Label(frame, text = "Ex: 20012345",font = ("Calibri", 14),bg='white').place(x=1100, y = 515)
   
    Label(frame, text="Password :",font = ("Calibri", 18),bg='white').place(x=700, y=570)   
    password_entry= Entry(frame, textvariable = password,
                          show="*",width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=615)
    Label(frame, text = "Ex: 21-OCT-2003",font = ("Calibri", 14),bg='white').place(x=1100, y = 610)
    
    login=HoverButton(frame,text = "Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=login_verify).place(x=750 , y=700)
    reset=HoverButton(frame,text = "Reset", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=reset).place(x=1000 , y=700)


def std_login():
    screen1.destroy()
    screen2=Tk()
    screen2.attributes('-fullscreen',True)  
    screen2.title("School Mangement System")

    Label(screen2,text = "DAV Public School, Pushpanjali Enclave" ,padx=290,pady=20, width = 50 , height = 100,
          font = ("times new roman", 45) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=0)
    Label(screen2,width = 1000 , height = 1, bg='white').place(x=0,y=120)
    Label(screen2,width =1 , height = 1000, bg='white').place(x=350,y=120)
    
    b1=HoverButton(screen2,text = "Profile", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                   activeforeground='white',font = ("Calibri", 28),command=stafflogin).place(x=0 , y=140)

    b2=HoverButton (screen2,text = "Fees" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=studentlogin).place(x=0 , y=218)

    b3=HoverButton (screen2,text = "Assignment" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=studentlogin).place(x=0 , y=296)


   
    screen2.mainloop()


    
def main_screen1():
    global canvas1,canvas2,l1,l2
   
    
    screen1.attributes('-fullscreen',True)  
    screen1.title("School Mangement System")

    Label(screen1,text = "Welcome to DAV Public School" ,padx=390,pady=20, width = 50 , height = 100,
          font = ("times new roman", 45) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=0)
    Label(screen1,width = 1000 , height = 1, bg='white').place(x=0,y=120)
    Label(screen1,width =1 , height = 1000, bg='white').place(x=350,y=120)
    
    canvas1 = Canvas(screen1, width = 900, height = 116)  
    canvas1.place(x=500,y=180)  
    img1 = ImageTk.PhotoImage(Image.open("dav_resized.png"))
    canvas1.create_image(0, 0, anchor=NW, image=img1) 
    
    canvas2 = Canvas(screen1, width = 900, height = 238)  
    canvas2.place(x=500,y=340)  
    img2 = ImageTk.PhotoImage(Image.open("Webp.net-resizeimage.png"))
    canvas2.create_image(0, 0, anchor=NW, image=img2)

    l2=Label(screen1,text = "We at D.A.V. believe in setting clear visions and challenges\n in keeping with the new millennium and laying a healthy\n foundation by creating a sustainable environment, that is the\n key to human existence...." ,
          width = 50 , height = 100,
          font = ("times new roman", 28) ,anchor=NW,
          bg='deepskyblue4',fg = "white")
    l2.place(x=500,y=650)

    b1=HoverButton(screen1,text = "Staff Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=stafflogin).place(x=0 , y=140)

    b2=HoverButton (screen1,text = "Student Login" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=studentlogin).place(x=0 , y=218)

    b3=HoverButton (screen1,text = "Photo Gallery" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=quit_screen).place(x=0 , y=296)

    b4=HoverButton (screen1,text = "About" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),).place(x=0 , y=374)
   
    b4=HoverButton (screen1,text = "Exit" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=quit_screen).place(x=0 , y=452)

   
   

   
    screen1.mainloop()
main_screen1()
