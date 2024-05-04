from customtkinter import * 
import threading
import facemain
from PIL import Image
#import numpy as np  
import os

 
def gui():
    def loginchecker():
        counter=0
        x=entry.get()
        entry.delete(0,END)
        print(x)
        password="xxx"
        if password==x:
           label.configure(text="Login was an Success")
           #tab1.destroy()
        else:
            if counter<=3:  
                label.configure(text= "Suspicion detected")
                print("failure ocuured")
            else:
                label.configure(text="Suspicion raised")
                counter=counter+1
                print("")
    global counter
    counter=0
    app = CTk()
    set_appearance_mode("dark")
    app.geometry("1920x1080")
    image = Image.open(r"F:\miniproject-main\miniproject-main\imagebase\kratos.jpg")
    background_image = CTkImage(image,size=(1920,1080))
    global label
    mytab=CTkTabview(master=app,height=700,width=700,)
    mytab.pack(padx=20, pady=20)
    tab1=mytab.add("  Login   ")
    tab2=mytab.add("  Signup  ")
    entry1= CTkEntry(tab1, corner_radius=32, placeholder_text="enter your username",width=150)
    entry1.pack(pady=100)
    entry= CTkEntry(tab1, corner_radius=32, placeholder_text="enter your password",width=150)
    entry.pack(pady=100)
    btn = CTkButton(tab1, text="Login",fg_color="#098080",corner_radius=32, hover_color="#C850C0",command=loginchecker)
    btn.place(relx=0.5,rely=0.5, anchor="center")
    label=CTkLabel(tab1,text="Login",anchor="center")
    label.place(relx=0.5,rely=0.6,anchor="center")
    
    app.mainloop()
#x1=threading.Thread(target=gui)
#x2=threading.Thread(target=facemain.facerecon)
gui()
#x1.start()
#x2.start()
