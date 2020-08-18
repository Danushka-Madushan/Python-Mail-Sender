from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import PySimpleGUI as sg
from sys import exit
import msvcrt as m
import smtplib
import sys
import time
import re
import os

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

banner = '''~Starting Alexa Mail Send Bot...
~Started...
~Please Enter Reciver's E-Mail Address below...'''

sg.theme('DarkAmber')
layout1 = [ [sg.Text('•Enter Recipient\'s Adress.')],
            [sg.InputText()],
            [sg.Text('•Validity       ',key="DOX")],
            [sg.Button('Submit Email')]]

layout2 = [ [sg.Text('•Enter Subject.')],
            [sg.InputText()],
            [sg.Button('Submit Subject')]]

layout3 = [ [sg.Text('•Enter Your Message.')],
            [sg.Multiline(size=(90, 20))],
            [sg.Button('Submit Mssage')]]

print("~Starting Alexa Mail Send Bot...")
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)

except Exception as Identifier:
    print(
        "~Initialization Faild!.\n~Please Check Your Internet Connection!")
    time.sleep(1.5)
    print("~Program Will Exit in 3 Seconds!")
    time.sleep(0.5)
    print_s("~Exiting..")
    time.sleep(1)
    exit()

fromaddr = "alexa.virtualassistent@gmail.com"
print("~Started...")
print("~Please Enter Recipient's E-Mail Address below...")
while(1):
    
    window = sg.Window('Recipient\'s Adress', layout1)
    while True:
        try:
            event, values = window.read()
            toaddr = values[0]
            x = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", toaddr)
            if not x:
                window['DOX'].update('•InValid!')
                continue
            if event == sg.WIN_CLOSED or event == 'Submit Email':
                break
        except Exception as Identifier:
            print("~You Terminated The Program..\n~Exting..")
            time.sleep(1)
            exit()
    window.close()
    try:
        if x:

            print("~Done!...")
            print("~Mail Will Be Sended To This Address : (" + toaddr + ")")
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            print("~Enter Subject ..")
            window = sg.Window('Subject', layout2)
            while True:
                    try:
                        event, values = window.read()
                        msg['Subject'] = values[0]
                        if event == 'Submit Subject':
                            break
                        if event == sg.WIN_CLOSED:
                            print("~You Terminated The Program..\n~Exting..")
                            time.sleep(1)
                            exit()
                    except Exception as Identifier:
                        print("~You Terminated The Program..\n~Exting..")
                        time.sleep(1)
                        exit()
            window.close()
            print("~Added!...")
            time.sleep(0.5)
            print("~Enter Message ..")
            window = sg.Window('Message', layout3)
            while True:
                    try:
                        event, values = window.read()
                        body = values[0]
                        if event == 'Submit Mssage':
                            break
                        if event == sg.WIN_CLOSED:
                            print("~You Terminated The Program..\n~Exting..")
                            time.sleep(1)
                            exit()
                    except Exception as Identifier:
                        print("~You Terminated The Program..\n~Exting..")
                        time.sleep(1)
                        exit()
            window.close()
            msg.attach(MIMEText(body, 'plain'))
            print("~Done!\n~Working...")
            time.sleep(2)
            s.starttls()
            print("~Authunticating...")
            try:
                passcode = "MyNameIsAlexa"
                s.login(fromaddr, passcode)
                print("~Confirmed!")
            except Exception as Identifier:
                print(
                    "~Authuntication Faild!\n~Please Contact Owner of This Program!")
                time.sleep(2)
                exit()

            text = msg.as_string()
            print("~Sending..")
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
            print("~Done!")
            print("~Press Any Button For Exit!..")
            m.getch()
            print("~Exiting!...")
            time.sleep(0.5)
            exit()

        else:
            print("~The E-Mail You  Enterd is Not Valid\n~Please Recheck..")
            time.sleep(1.5)
            os.system("cls")
            print(banner)
            continue

    except KeyboardInterrupt:
        print("~Canceled by USER!")
        exit()