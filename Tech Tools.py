import subprocess

from tkinter import *

def click():
    print("Launching MalwareBytes!")
    subprocess.run(['MBSetup.exe'], shell=True)
    button.config(bg='white')

def click1():
    print("Launching SIW!")
    subprocess.run(['siw\\siw.exe'], shell=True)
    button1.config(bg='white')

def click2():
    print("Launching CystalDisk!")
    subprocess.run(['CrystalDiskInfo7_1_1\\DiskInfo64.exe'], shell=True)
    button2.config(bg='white')
    
def click3():
    print("Launching SmartDefrag!")
    subprocess.run(['SmartDefragPortable\\SmartDefragPortable.exe'], shell=True)
    button3.config(bg='white')

def click4():
    print("Launching ADWCleaner!")
    subprocess.run(['adwcleaner.exe'], shell=True)
    button4.config(bg='white')

def click5():
    print("Launching HerdProtect!")
    subprocess.run(['herdProtectScan_Portable.exe'], shell=True)
    button5.config(bg='white')

def click6():
    print("Launching HitmanPro!")
    subprocess.run(['HitmanPro_x64.exe'], shell=True)
    button6.config(bg='white')
    
def click7():
    print("Launching RogueKiller!")
    subprocess.run(['RogueKiller_portable64.exe'], shell=True)  
    button7.config(bg='white')
    
def click8():
    print("Launching TDSSKiller!")
    subprocess.run(['TDSSKiller.exe'], shell=True)
    button8.config(bg='white')

def click9():
    print("Launching TFC!")
    subprocess.run(['TFC.exe'], shell=True)
    button9.config(bg='white')
    
window = Tk()
window.title('Alpha Tech Tools by Chris Page')
window.geometry('300x450+50+50')
window.resizable(False, False)
window.configure(bg='black')
img = PhotoImage(file="PBack.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)
title = Label(window, text = "Alpha's Tech Tools")
title.config(font=('INK FREE' , 10,'bold'))
button = Button(window,text='MalwareBytes', bg='blue', fg='white')
button1 = Button(window,text='SIW', bg='blue', fg='white')
button2 = Button(window,text='CrystalDisk', bg='blue', fg='white')
button3 = Button(window,text='SmartDefrag', bg='blue', fg='white')
button4 = Button(window,text='ADWCleaner', bg='blue', fg='white')
button5 = Button(window,text='HerdProtect', bg='blue', fg='white')
button6 = Button(window,text='HitmanPro', bg='blue', fg='white')
button7 = Button(window,text='RogueKiller', bg='blue', fg='white')
button8 = Button(window,text='TDSSKiller', bg='blue', fg='white')
button9 = Button(window,text='TFC', bg='blue', fg='white')
title.pack()
button2.config(command=click2)
button2.config(font=('INK Free' ,15,'bold'))
button2.pack()
button4.config(command=click4)
button4.config(font=('INK Free' ,15,'bold'))
button4.pack()
button.config(command=click)
button.config(font=('INK Free' ,15,'bold'))
button.pack()
button7.config(command=click7)
button7.config(font=('INK Free' ,15,'bold'))
button7.pack()
button5.config(command=click5)
button5.config(font=('INK Free' ,15,'bold'))
button5.pack()
button8.config(command=click8)
button8.config(font=('INK Free' ,15,'bold'))
button8.pack()
button9.config(command=click9)
button9.config(font=('INK Free' ,15,'bold'))
button9.pack()
button7.config(command=click7)
button7.config(font=('INK Free' ,15,'bold'))
button7.pack()
button3.config(command=click3)
button3.config(font=('INK Free' ,15,'bold'))
button3.pack()
button6.config(command=click6)
button6.config(font=('INK Free' ,15,'bold'))
button6.pack()
button1.config(command=click1)
button1.config(font=('INK Free' ,15,'bold'))
button1.pack()
window.mainloop()

