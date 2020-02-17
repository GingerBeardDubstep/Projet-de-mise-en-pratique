#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from tkinter import *
import pickle
from fonctions.fonctionsInterface import *
from classes.Joueur import *
"""from interface_graphique.InterfaceUtilisateur import *
from interface_graphique.InterfaceInscription import *"""
import time

class InterfaceConnexion(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre,serveur, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.serveur=serveur
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.messagenoConnect = Label(self, text="Mot de passe ou login erroné", fg = "red")
		self.reinitTot()
		# Création de nos widgets
		

	def reinit(self,log) :
		self.message["text"] = "Bienvenue "+log
		self.bouton_retour = Button(self, text="Se déconnecter",command=self.reinitTot())
		self.ligne_log.destroy()
		self.ligne_key.destroy()
		self.bouton_co.destroy()
		self.bouton_re.destroy()
		self.bouton_retour.pack()


	def connexion(self) :
		login = self.var_log.get()
		mdp = self.var_key.get()
		self.serveur.send(b"tentative connexion")
		time.sleep(0.1)
		self.serveur.send(login.encode())
		time.sleep(0.1)
		self.serveur.send(mdp.encode())
		retour = pickle.loads(self.serveur.recv(1024))
		if(retour == "False") :
			self.message = Label(self, text="Mot de passe ou login erroné")
		else :
			lancerInterfaceUtilisateur(self.serveur,self.fenetre,self,self.retour)


	def reinitTot(self) :
		self.message = Label(self, text="Connectez-vous ou créez un compte.")
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

		self.bouton_co = Button(self, text="Connectez vous", fg="red", command=self.connexion)
		self.bouton_co.pack(side="left")
		self.bouton_re = Button(self, text="Inscrivez vous", fg="red", command=self.inscription)
		self.bouton_re.pack(side="right")

		self.bouton_quitter = Button(self, text="Quitter", command=self.quitter)
		self.bouton_quitter.pack(side="bottom")
        
		
		if(self.bouton_retour is not None) :
			self.bouton_retour.destroy()

	def quitter(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.quit()

	def inscription(self) :
		lancerInterfaceInscription(self,self.fenetre,self.serveur)

	def register(self) :
		tst = False
		clef = self.var_key.get()
		log = self.var_log.get()
		comptes = lire()
		for cle,val in comptes.items() :
			if(cle == log) :
				tst=True
		if(tst) :
			self.message["text"] = "Ce loggin existe déjà"
		else :
			comptes[log] = clef
			editer(comptes)

"""def lancerInterfaceInscription(frame,fenetre,serveur) :
	frame.destroy()
	interface = InterfaceInscription(fenetre,serveur)

	interface.mainloop()
	interface.destroy()

def lancerInterfaceUtilisateur(frame,fenetre,serveur,joueur) :
	frame.destroy()
	interface = InterfaceUtilisateur(fenetre,serveur,joueur)

	interface.mainloop()
	interface.destroy()

def essaiConnexion(frame,fenetre,login,mdp,serveur) :
	serveur.send(b"tentative connexion")
	time.sleep(0.1)
	serveur.send(login.encode())
	time.sleep(0.1)
	serveur.send(mdp.encode())
	retour = serveur.recv(1024).decode()
	if(retour == "False") :
		try :
			frame.messagenoConnect.destroy()
		except NameError :
			pass
		frame.messagenoConnect = Label(frame, text="Mot de passe ou login erroné", fg = "red")
		frame.messagenoConnect.pack(side="top")
	else :
		lancerInterfaceUtilisateur(serveur,fenetre,retour)"""

