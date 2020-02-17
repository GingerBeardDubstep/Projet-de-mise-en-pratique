#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from tkinter import *
import os
import pickle
from fonctions.fonctionsInterface import *
#from interface_graphique.InterfaceConnexion import InterfaceConnexion

class InterfaceIntermediaire(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre,serveur, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.serveur=serveur
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.message = Label(self, text="Bravo ! Vous êtes bien inscrits")
		self.message.pack()

		self.message2 = Label(self, text="Appuyez sur le bouton pour revenir à l'écran de connexion")
		self.message2.pack()

		self.bouton_re = Button(self, text="Retour connexion", command=self.retour)
		self.bouton_re.pack()

		self.bouton_quitter = Button(self, text="Quitter", fg="red", command=self.quitter)
		self.bouton_quitter.pack()		# Création de nos widgets

	def quitter(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.quit()

	def retour(self) :
		retourInterface(self,self.fenetre,self.serveur)