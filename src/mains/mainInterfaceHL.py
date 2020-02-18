#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from classes.Joueur import *
from tkinter import *
from interface_graphique.InterfaceHorsLigne import *

fenetre = Tk()
instance = InterfaceHorsLigne(fenetre)
instance.mainloop()