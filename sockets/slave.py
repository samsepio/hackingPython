import socket
from colorama import *
import subprocess

def slave():
    mi_socket=socket.socket();
    mi_socket.connect(('localhost',8000));
    mi_socket.send("hola que backdor tan buena".encode());
    respuesta=mi_socket.recv(1024);
    print(respuesta);
    mi_socket.close();
slave();
