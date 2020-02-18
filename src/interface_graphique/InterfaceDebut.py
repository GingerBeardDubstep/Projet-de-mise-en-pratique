#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from tkinter import *
from classes.Joueur import *
from fonctions.fonctionsInterface import *
from interface_graphique.InterfaceEnLigne import *
import os

class InterfaceDebut(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		background = PhotoImage(file = "../images_interface/background_depart.png",master=self)
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.message = Label(self, text="BattleShip")
		self.message.pack(side="top")
		self.message_charge = Label(self,text="Chargement")


		self.bouton_hl = Button(self, text="Partie hors-ligne", fg="green", command=self.horsLigne)
		self.bouton_hl.pack(side="left")

		self.bouton_re = Button(self, text="Partie en ligne", command=self.enLigne)
		self.bouton_re.pack(side="right")

		self.bouton_quitter = Button(self, text="Quitter", fg="red", command=self.quitter)
		self.bouton_quitter.pack()		# Création de nos widgets

	def quitter(self) :
		self.quit()

	def enLigne(self) :
		self.destroy()
		self.fenetre.destroy()
		os.system("python3.8 -m mains.mainInterfaceCo")
		os._exit(0)

	def horsLigne(self) :
		self.destroy()
		self.fenetre.destroy()
		os.system("python3.8 -m mains.mainInterfaceHL")
		os._exit(0)

def lancerInterfaceDebut() :
	fenetre = Tk()
	interface = InterfaceDebut(fenetre)

	interface.mainloop()
	interface.destroy()


