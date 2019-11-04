import smtplib
import getpass
from colorama import *
import subprocess

def sendmail():
    subprocess.run(['clear']);
    email=input(Fore.GREEN+"correo electronico: ");
    contraseña=getpass.getpass("contraseña: ");
    destinatario=input("destinatario: ");
    mensaje=input("mensaje: ");
    server=smtplib.SMTP('smtp.gmail.com','587');
    server.starttls();
    try:
        server.login(email,contraseña);
        server.sendmail(email,destinatario,mensaje);
        print(Fore.BLUE+"mensaje enviado correctamente!! ");
    except KeyboardInterrupt:
        print(Fore.RED+"\nfinalisado!!!");
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+"\ncontraseña incorrecta!!");
sendmail();
