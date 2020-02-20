#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from tkinter import *
import pickle
from classes.Joueur import *
from classes.Damier import *
from classes.Partie import *
#from interface_graphique.InterfaceEnLigne import *
import socket
import os
import time
from fonctions.fonctionsInterface import *

class InterfaceHorsLigne(Frame) :
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.joueur = Joueur("__localhost__")
		try :
			file=open("../localdata/dataJoueur","rb")
		except FileNotFoundError :
			self.joueur = Joueur("__localhost__")
			with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur,file)
		else :
			self.joueur = pickle.load(file)
		finally :
			self.pack(fill=BOTH)
			self.reinitTot()

		
		# Création de nos widgets
		

#3A37666FACCADE7D47AC6C6F34

	def jouer(self) :
		self.destroy()
		instance = InterfaceJeuHL(self.fenetre,self.joueur)
		


	def reinitTot(self) :
		
		self.message = Label(self, text="Bienvenue "+self.joueur.pseudo)
		self.message.pack(side="top")


		self.bouton_co = Button(self, text="Lancez une partie !", fg="white",background="blue", command=self.lancerJeu)
		self.bouton_co.pack()
		self.bouton_quitter = Button(self, text="Quitter", command=self.quitter)
		self.bouton_quitter.pack(side="bottom")

	def quitter(self) :
		"""with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur)"""
		self.destroy()
		self.fenetre.destroy()

	def lancerJeu(self) :
		if(self.joueur.pseudo=="__localhost__") :
			self.destroy()
			interface = InterfaceQuestion(self.fenetre)
			interface.mainloop()
		else :
			self.destroy()
			instance = InterfacePlacerHL(self.fenetre,self.joueur)
			instance.mainloop()

class InterfacePlacerHL(Frame) :
	def __init__(self,fenetre,joueur,**kwargs) :
		fenetre.geometry("800x800")
		self.fenetre=fenetre
		Frame.init(self,fenetre,width=800,height=800,**kwargs)
		self.damierJoueur = Damier()
		self.damierIA = Damier()
		self.damierIA.remplissageRandom()


class InterfaceQuestion(Frame) :
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.pack(fill=BOTH)
		self.reinitTot()
		# Création de nos widgets

	def reinitTot(self) :
		self.message = Label(self, text="Pour sauvegarder votre progression hors-ligne, il faut vous inscrire.")
		self.message.pack(side="top")

		self.bouton_co = Button(self, text="Inscrivez-vous !",fg="green", command=self.lancerInscription)
		self.bouton_co.pack(side="left")
		self.bouton_re = Button(self, text="Jouer sans sauvegarde", fg="red", command=self.lancerJeuHL)
		self.bouton_re.pack(side="right")
		self.bouton_quitter = Button(self, text="Quitter", command=self.quitter)
		self.bouton_quitter.pack(side="bottom")

	def quitter(self) :
		"""with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur)"""
		self.destroy()
		self.fenetre.destroy()

	def lancerInscription(self) :
		self.destroy()
		try :
			serveur = initialiserClient()
		except ConnectionRefusedError :
			self.destroy()
			self.fenetre.destroy()
			os.system("python3.8 -m mains.mainDebut")
			print("serveur hors-ligne")
			os._exit(1)
		else :
			instance = InterfaceInscription(self.fenetre,serveur)
			instance.mainloop()

		"""os.system("python3.8 -m mains.mainInterfaceInscr")
		os._exit(0)"""

	def lancerJeuHL(self) :
		self.destroy()
		instance = InterfaceJeuHL(self.fenetre,Joueur("__localhost__"))
		instance.mainloop()


