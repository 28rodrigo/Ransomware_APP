from utils.encrypt import Encryption


def encrypt_data(data:str):
    enc=Encryption("my_password")
    cypher=enc.encrypt_data(data)

    decoded=enc.decrypt_data(cypher)
    print(decoded)
#encrypt_data("hello world")

def encrypt_folder(path):
    enc=Encryption("my_password")
    enc.encrypt_folder(path)


encrypt_folder("files_to_encrypt")
