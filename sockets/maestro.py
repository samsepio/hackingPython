import socket
from colorama import *
import subprocess

def master():
    mi_socket=socket.socket();
    mi_socket.bind()
