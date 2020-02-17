#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from tkinter import *
import os
import pickle
from fonctions.fonctionsInterface import *

class InterfaceUtilisateur(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre,serveur,joueur, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.serveur=serveur
		self.joueur = joueur
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.message = Label(self, text="Bienvenue "+str(self.joueur.pseudo))
		self.message.pack()


		self.bouton_quitter = Button(self, text="Quitter", fg="red", command=self.quitter)
		self.bouton_quitter.pack()		# Création de nos widgets

	def quitter(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.quit()

	def envoi(self) :
		essaiInscription(self,self.var_log.get(),self.var_key.get(),self.var_pseudo.get(),self.serveur)