import urllib,urllib.request
from colorama import *
import shutil
import time
import subprocess

def downloadcode():
    inicio=time.time();
    subprocess.run(['clear']);
    try:
        url=input(Fore.GREEN+"url: ");
        nombre=input(Fore.GREEN+"nombre: ");
        print(Fore.YELLOW+"../descargando../");
        html_handler=urllib.request.urlopen(url);
        html_file=str(html_handler.read(),'utf-8');
        html=open(nombre,'w');
        html.write(html_file);
        final=time.time();
        print(Fore.BLUE+"descargado correctamente!!!");
    except KeyboardInterrupt:
        print(Fore.RED+"\nfinalisado!!");
    except urllib.error.URLError:
        print(Fore.RED+"\nurl no valida");;
downloadcode();

