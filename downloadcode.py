import urllib,urllib.request
from colorama import *
import subprocess

def downloadcode():
    subprocess.run(['clear']);
    url=input(Fore.GREEN+"url: ");
    nombre=input("nombre: ");
    try:
        print(Fore.YELLOW+"descargando "+url+"../");
        html_handler=urllib.request.urlopen(url);
        html_file=str(html_handler.read(),'utf-8');
        archivo=open(nombre,'w');
        archivo.write(html_file);
        print(Fore.BLUE+"descargado completamente!!!");
    except KeyboardInterrupt:
        print(Fore.RED+"\nFinalisado!!!");
    except urllib.error.HTTPError:
        print(Fore.RED+"\nurl no encontrada");
downloadcode();


