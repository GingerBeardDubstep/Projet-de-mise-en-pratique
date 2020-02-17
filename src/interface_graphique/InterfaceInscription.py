#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from tkinter import *
import os
import pickle
from fonctions.fonctionsInterface import *
import time
from classes.exceptions.ExceptionsConnexion import *

class InterfaceInscription(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre,serveur, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.serveur=serveur
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.message = Label(self, text="Inscription.")
		self.message.pack()

		self.message2 = Label(self, text="Login")
		self.message2.pack()


		self.var_log = StringVar()
		self.ligne_log = Entry(self, textvariable=self.var_log, width=30)
		self.ligne_log.pack()

		self.message3 = Label(self, text="Mot de passe")
		self.message3.pack()

		self.var_key = StringVar()
		self.ligne_key = Entry(self, textvariable=self.var_key, width=30)
		self.ligne_key.pack()

		self.message4 = Label(self, text="Pseudo")
		self.message4.pack()

		self.var_pseudo = StringVar()
		self.ligne_pseudo = Entry(self, textvariable=self.var_pseudo, width=30)
		self.ligne_pseudo.pack()

		self.bouton_in = Button(self, text="Inscription", fg="green", command=self.envoi)
		self.bouton_in.pack()

		self.bouton_re = Button(self, text="Retour connexion", command=self.retour)
		self.bouton_re.pack()

		self.bouton_quitter = Button(self, text="Quitter", fg="red", command=self.quitter)
		self.bouton_quitter.pack()		# Création de nos widgets

	def quitter(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.quit()

	def envoi(self) :
		essaiInscription(self,self.fenetre,self.var_log.get(),self.var_key.get(),self.var_pseudo.get(),self.serveur)

	def retour(self) :
		retourInterface(self,self.fenetre,self.serveur)

def essaiInscription(frame,fenetre,login,mdp,pseudo,serveur) :
	serveur.send(b"tentative inscription")
	time.sleep(0.1)
	serveur.send(login.encode())
	time.sleep(0.1)
	serveur.send(mdp.encode())
	time.sleep(0.1)
	serveur.send(pseudo.encode())
	retour = serveur.recv(1024).decode()
	if(retour == "False login") :
		fenetre.message = Label(self,text="Ce login est déjà utilisé")
	elif(retour == "False pseudo") :
		fenetre.message = Label(self,text="Ce pseudo est déjà utilisé")
	elif(retour == "False encodage") :
		fenetre.message = Label(self,text="Veuillez tout changer")
	elif(retour == "Done") :
		lancerInterfaceIntermediaire(frame,fenetre,serveur)
	else :
		raise CommunicationError("Message inattendu")

def lancerInterfaceIntermediaire(frame,fenetre,serveur) :
	frame.destroy()
	interface = InterfaceIntermediaire(fenetre,serveur)

	interface.mainloop()
	interface.destroy()

def retourInterface(frame,fenetre,serveur) :
	frame.destroy()
	interface = InterfaceConnexion(fenetre,serveur)

	interface.mainloop()
	interface.destroy()


