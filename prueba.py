#--------------------------------------Importamos librerias--------------------------------------------

from tkinter import *
from tkinter import messagebox as msg
import os
import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
import numpy as np
import database as db

# CONFIG 
path = "C:\Users\pagin\login-registro-facial"

txt_login  = "LOGIN"
txt_registro = "REGISTRO"

color_white = "#F4F5F4"
color_black = "#151515"

color_black_btn = "#202020"
color_background = "#151515"

font_label = "century gothic"
size_screen = "500x300"

# COLORS 
color_success = "\033[1;32;40m"
color_error = "\033[1;31;40m"
color_normal = "\033[0;37;40m"

res_bd = {"id": 0, "affected": 0} # database variable

# --------------------------------------Funciones--------------------------------------------

def getEnter(screen):
    Label(screen, text= "", bg=color_background).pack()

def printAndShow(screen, text, flag):
    if flag:
        print(color_success + text + color_normal)
        screen.destroy()
        msg.showinfo8(message = text, tittle = "Exito!")
    else:
        print(color_error + text + color_normal)
        Label(screen, text="", fg="red", bg=color_background, font= (font_label, 12)).pack()

def configure_screen(screen, text):
    screen.tittle(text),
    screen.geometry(size_screen),
    screen.configure(bg=color_background)
    Label(screen, text=f"¡{text}!", fg=color_white, bg=color_black, font=(font_label, 18), width="500", height="2").pack()

def credentials(screen, var, flag):
    Label(screen, text="Usuario", fg="red", bg=color_background, font= (font_label, 12)).pack()
    entry = entry(screen, textvariable=var, justify="center", font=(font_label, 12))
    entry.focus_force()
    entry.pack(side=TOP, ipadx=30, ipady=6)
    
    getEnter()

    if flag:
        Button(screen, text="Capturar Rostro", fg=color_white, bg=color_black_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command="login_capture").pack()
    else:
        Button(screen, text="Registrar Rostro",  fg=color_white, bg=color_black_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command="register_capture").pack
    
    return entry