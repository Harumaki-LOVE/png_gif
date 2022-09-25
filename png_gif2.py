import PIL.Image
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

files = sorted(glob.glob('./20220922/*.png')) 
images = list(map(lambda file : PIL.Image.open(file) , files))
images[0].save('./image.gif',save_all = True , append_images = images[1:] , duration = 400 , loop = 0)