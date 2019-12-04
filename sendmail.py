from colorama import *
import smtplib
import subprocess
import getpass

def sendmail():
    subprocess.run(['clear']);
    correo=input(Fore.GREEN+"correo: ");
    contraseña=getpass.getpass("contraseña: ");
    destinatario=input("destinatario: ");
    mensaje=input("mensaje: ");
    try:
        print(Fore.YELLOW+"enviando mensaje a "+correo+"../");
        server=smtplib.SMTP('smtp.gmail.com','587');
        server.starttls();
        server.ehlo();
        server.login(correo,contraseña);
        server.sendmail(correo,destinatario,mensaje);
        server.quit();
    except KeyboardInterrupt:
        print(Fore.RED+"\nfinalisado!!!");
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+"\ncontraseña incorrecta");
sendmail();
