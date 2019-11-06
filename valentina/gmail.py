import smtplib
from colorama import *
import subprocess
import getpass
import os

def sendmail():
    subprocess.run(['clear']);
    try:
        email=input(Fore.GREEN+"correo electronico: ");
        contraseña=getpass.getpass("contraseña: ");
        destino=input("destinatario: ");
        mensaje=input("mensaje: ");

        server=smtplib.SMTP('smtp.gmail.com','587');
        server.starttls();
        server.login(email,contraseña);
        server.sendmail(correo,destino,mensaje);
        server.quit();
    except KeyboardInterrupt:
        print(Fore.RED+"\nFinalisado!!");
    except smtplib.SMTPAuthenticationError:
        print("\ncontraseña incorrecta");
sendmail();
