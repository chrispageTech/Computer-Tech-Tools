import subprocess
import shelve
from tkinter import *

def launch_application(executable):
    subprocess.run([executable], shell=True)
    button.config(bg='white')

def save_selected_buttons():
    # Open the shelf database
    db = shelve.open("selected_buttons")
    # Get the indices of all selected buttons
    selected_indices = [i for i, chk in enumerate(checkboxes) if chk.get() == 1]
    # Save the selected indices to the shelf database
    db["selected_indices"] = selected_indices
    db.close()

def load_selected_buttons():
    # Open the shelf database
    db = shelve.open("selected_buttons")
    # Load the selected indices from the shelf database
    selected_indices = db.get("selected_indices", [])
    # Set the checkboxes for the selected indices to be checked
    for i in selected_indices:
        checkboxes[i].set(1)
    db.close()

window = Tk()
window.title('Alpha Tech Tools by Chris Page')
window.geometry('300x600+50+50')
window.resizable(False, False)
window.configure(bg='black')
img = PhotoImage(file="PBack.png")
Label(window, image=img).grid(row=0, column=0, columnspan=2, sticky='w')
Label(window, text = "Alpha's Tech Tools", font=('INK FREE', 10,'bold')).grid(row=1, column=0, columnspan=2, sticky='w')

# Create a list to store the checkboxes
checkboxes = []

buttons = [
    Button(window, text='MalwareBytes', bg='blue', fg='white', command=lambda: launch_application('MBSetup.exe')),
    Button(window, text='SIW', bg='blue', fg='white', command=lambda: launch_application('siw\\siw.exe')),
    Button(window, text='CrystalDisk', bg='blue', fg='white', command=lambda: launch_application('CrystalDiskInfo7_1_1\\DiskInfo64.exe')),
    Button(window, text='SmartDefrag', bg='blue', fg='white', command=lambda: launch_application('SmartDefragPortable\\SmartDefragPortable.exe')),
    Button(window, text='ADWCleaner', bg='blue', fg='white', command=lambda: launch_application('adwcleaner.exe')),
    Button(window, text='HerdProtect', bg='blue', fg='white', command=lambda: launch_application('herdProtectScan_Portable.exe')),
    Button(window, text='HitmanPro', bg='blue', fg='white', command=lambda: launch_application('HitmanPro_x64.exe')),
    Button(window, text='RogueKiller', bg='blue', fg='white', command=lambda: launch_application('RogueKiller_portable64.exe')),
    Button(window, text='TDSSKiller', bg='blue', fg='white', command=lambda: launch_application('TDSSKiller.exe')),
    Button(window, text='TFC', bg='blue', fg='white', command=lambda: launch_application('TFC.exe'))
]

for i, button in enumerate(buttons):
    # Create a checkbox for each button
    chk = IntVar()
    chk_btn = Checkbutton(window, variable=chk)
    # Add the checkbox to the grid
    chk_btn.grid(row=i, column=0, sticky='w')
    checkboxes.append(chk)
    # Add the button to the grid
    button.grid(row=i, column=1, sticky='w')

# Add a "Save" button at the bottom of the window
save_button = Button(window, text="Save", command=save_selected_buttons)
save_button.grid(row=len(buttons), column=0, columnspan=2, sticky='w')

# Add a "Load" button at the bottom of the window
load_button = Button(window, text="Load", command=load_selected_buttons)
load_button.grid(row=len(buttons)+1, column=0, columnspan=2, sticky='w')

# Make the buttons and checkboxes take up the full width of the window
for i in range(len(buttons)+2):
    window.columnconfigure(i, weight=1)

window.mainloop()
