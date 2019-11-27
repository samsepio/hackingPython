import socket
from colorama import *
import subprocess

def socket():
    opcion=input("maestro o esclavo: ");
    if(opcion=="m"or opcion=="M"):
        host=input("host: ");
        puerto=input("puerto: ");
        mi_socket=socket.socket();
        mi_socket.bind((host,puerto));
        mi_socket.listen(2);
        while True:
            conexion,addr=mi_socket.accept();
            print(addr)
            print("nueva conexion establecida");
            conexion.send("creare una backdor".encode());
            conexion.close();
    if(opcion=="e"or opcion=="E"):
        hostE=input("host: ");
        puertoE=input("puerto: ");
        misocket=socket.socket();
        misocket.connect((host,puerto));
        misocket.send("que buen script".encode());
        respuesta=misocket.recv(1024);
        print(respuesta);
        misocket.close();
socket();
