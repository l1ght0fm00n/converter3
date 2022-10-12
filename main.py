from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image


def choosefile():
    pass


def choosefile_test():
    pass

    global filename
    Tk().withdraw()
    filename = askopenfilename()
