# Buga Tamás 
# Python
# Employers Login / Register System 



# Imports
#====================================

from tkinter import *
from tkinter import ttk
import os
from tkinter.tix import COLUMN

os.system('cls')

root = Tk()
root.geometry('500x500')
root.title('Company-name Employer System')

mainFrame = ttk.Frame(root, padding=10).grid()
mainLabel = ttk.Label(mainFrame, text = 'Welcome').grid(column = 0, row = 0)
mainButton = ttk.Button(mainFrame, text = 'Quit', command = root.destroy).grid(column=2, row=0)

root.mainloop()


# Functions here
#====================================




# Program start
#====================================