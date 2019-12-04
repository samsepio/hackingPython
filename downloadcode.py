from colorama import *
import urllib,urllib.request
import subprocess

def downloadcode():
    subprocess.run(['clear']);
    url=input(Fore.GREEN+"url: ");
    nombre=input(Fore.GREEN+"nombre: ");
    try:
        print(Fore.YELLOW+"descargando "+url+".../")
        html_handler=urllib.request.urlopen(url);
        html_file=str(html_handler.read());
        archivo=open(nombre,'w');
        archivo.write(html_file);
        print(Fore.BLUE+"descargado correctamente!!");
    except KeyboardInterrupt:
        print(Fore.RED+"\nfinalisado!!!");
downloadcode();
