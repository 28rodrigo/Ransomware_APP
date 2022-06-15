#!/usr/bin/python3
import sys
import base64, hashlib
from cryptography.fernet import Fernet
from codecs import utf_8_decode
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



#print(len(sys.argv), 'arguments.')
#print("ARGS: ",sys.argv[1])
enc= Encryption(sys.argv[1])
enc.decrypt_folder('/opt/files_to_encrypt')
val = input("Python:Enter your value: ")

print("PYTHON:Hello: ",val)
print("PYTHON:BYE")
