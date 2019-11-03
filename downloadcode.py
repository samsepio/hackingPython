import urllib,urllib.request
from colorama import *
import shutil
import subprocess

def downloadcode():
    subprocess.run(['clear']);
    url=input(Fore.GREEN+"url: ");
    nombre=input("nombre: ");
    ubicacion=input("ubicacion: "); 
    print(Fore.YELLOW+"../Descargando../");
    html_handler=urllib.request.urlopen(url);
    html_file=str(html_handler.read(),'utf-8');
    codigo=open(nombre,'w');
    #shuti.move(archivo,ubicacion);
    codigo.write(html_file);
    codigo.close();
    print(Fore.BLUE+"descargado!!!");
downloadcode();

