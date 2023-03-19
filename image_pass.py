import random
import tkinter as tk
from turtle import width
from PIL import Image,ImageTk
from setuptools import Command


#encryptions
def encryption():
    from cryptography.fernet import Fernet
 

    PASS = "Atanu"

    
 

 
    key = Fernet.generate_key()
 

 
    fernet = Fernet(key)
 

    encMessage = fernet.encrypt(PASS.encode())
 

 

    decMessage = fernet.decrypt(encMessage).decode()
 
    
    
    output.insert(0,("Authenticated "+decMessage))

win = tk.Tk()

# win.geometry("700x300")

pawd=[]

BN1_c = 0
BN2_c = 0
BN3_c = 0

def B1():
    pawd.append(1)

def B2():
    pawd.append(2)

def B3():
    pawd.append(3)

def cal():
    global pawd
    output.delete(0,tk.END)
    if (pawd[0]==1 and pawd[1]==2 and pawd[2]==3):
        encryption()
        # output.insert(0,("authorized"))
        pawd = []
    else:
        output.insert(0,("unauthorized"))
        pawd = []

img1= (Image.open("img/flo.webp"))
resized_image1= img1.resize((100,100))
B1_image= ImageTk.PhotoImage(resized_image1)

img2= (Image.open("img/house.png"))
resized_image2= img2.resize((100,100))
B2_image= ImageTk.PhotoImage(resized_image2)

img3= (Image.open("img/dianosor.webp"))
resized_image3= img3.resize((100,100))
B3_image= ImageTk.PhotoImage(resized_image3)

a=random.randint(0,2)

arrsuf=['N','W','E']
var1 = arrsuf[a]
arrsuf.remove(arrsuf[a])

a=random.randint(0,1)
var2 = arrsuf[a]
arrsuf.remove(arrsuf[a])

var3=arrsuf[0]

Btn1 = tk.Button(win, image=B1_image, width=100, height=100,command=B1)
Btn1.grid(row=0,sticky=var1)

Btn2 = tk.Button(win, image=B2_image, width=100, height=100,command=B2)
Btn2.grid(row=0,sticky=var2)

Btn3 = tk.Button(win, image=B3_image, width=100, height=100,command=B3)
Btn3.grid(row=0,sticky=var3)

Enter = tk.Button(win,text="Enter",width=2,height=1,command=cal)
Enter.grid(row=1,column=0,sticky=tk.EW)

output =tk.Entry(win,width=40)
output.grid(row=2,column=0,pady=10,padx=10,sticky=tk.E)


win.mainloop()
