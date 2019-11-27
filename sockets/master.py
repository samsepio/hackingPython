import socket
from colorama import *
import subprocess

def master():
    mi_socket=socket.socket();
    mi_socket.bind(('localhost',8000));
    mi_socket.listen(5);
    while True:
        conexion, addr = mi_socket.accept()
        print(Fore.GREEN+"Nueva conexion establecida");
        print(addr);
        conexion.send("creare una backdor".encode());
        conexion.close();
master();
