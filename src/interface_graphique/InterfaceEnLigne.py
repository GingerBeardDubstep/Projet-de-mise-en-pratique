#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from tkinter import *
import pickle
from classes.Joueur import *
from classes.StructureJoueurs import *
from interface_graphique.InterfaceHorsLigne import *
import socket
import os
import time

argFonfNoir = dict()
argFonfNoir["fg"] = "white"
argFonfNoir["background"] = "black"

class InterfaceConnexion(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre,serveur, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2),background="black", **kwargs)
		self.serveur=serveur
		self.pack(fill=BOTH)
		self.bouton_retour = None
		self.messagenoConnect = Label(self, text="Mot de passe ou login erroné", fg = "red")
		self.reinitTot()
		# Création de nos widgets

	def connexion(self) :
		try :

			login = self.var_log.get()
			mdp = self.var_key.get()
			if(self.var_case.get()==1) :
				with open("../localdata/identifiants","wb") as file :
					_temp = (login,mdp)
					pickle.dump(_temp,file)
			else :
				os.system("rm -f ../localdata/identifiants")
			self.serveur.send(b"tentative connexion")
			time.sleep(0.1)
			self.serveur.send(login.encode())
			time.sleep(0.1)
			self.serveur.send(mdp.encode())
			retour = self.serveur.recv(1024)
			
			if(retour == b"False") :
				self.message.config(text="Mot de passe ou login errone",fg="red")
				self.ligne_log.config(background="red")
				self.ligne_key.config(background="red")
			else :
				retour = pickle.loads(retour)
				with open("../localdata/dataJoueur","wb") as file :
					pickle.dump(retour,file)
				lancerInterfaceUtilisateur(self,self.serveur,self.fenetre,retour)
		except BrokenPipeError :
			print("serveur hors-ligne")
			self.serveur.close()
			self.destroy()
			self.fenetre.destroy()
			os._exit(1)
		


	def reinitTot(self) :
		try :
			file = open("../localdata/identifiants","rb")
			file.close()
		except FileNotFoundError :
			self.var_log = StringVar()
			self.ligne_log = Entry(self, textvariable=self.var_log,justify="center", width=30)
			#self.ligne_log.pack()

			self.var_key = StringVar()
			self.ligne_key = Entry(self, textvariable=self.var_key,justify="center", width=30,show="*")
			#self.ligne_key.pack()

			self.var_case = IntVar()
			self.case = Checkbutton(self, text="Se souvenir de moi", variable=self.var_case,**argFonfNoir)
			#self.case.pack(side="top")
		else :
			log=""
			mdp=""
			with open("../localdata/identifiants","rb") as file :
				log,mdp = pickle.load(file)
			self.var_log = StringVar()
			self.ligne_log = Entry(self, textvariable=self.var_log,justify="center", width=25)
			self.var_log.set(log)
			#self.ligne_log.pack()

			self.var_key = StringVar()
			self.ligne_key = Entry(self, textvariable=self.var_key,justify="center", width=25,show="*")
			self.var_key.set(mdp)
			#self.ligne_key.pack()

			self.var_case = IntVar()
			self.var_case.set(1)
			self.case = Checkbutton(self, text="Se souvenir de moi", variable=self.var_case)
			#self.case.pack(side="top")
		finally :
			"""self.cadreSup = Label(self,text="BattleShip",width=60,height=5)
			self.cadreSup.pack(side="top",fill=X,padx=0,pady=0,ipadx=0,ipady=0)"""
			self.message = Label(self, text="Connectez-vous ou créez un compte.",**argFonfNoir)
			self.message.pack()

			self.message2 = Label(self, text="Login",**argFonfNoir)
			self.message2.pack()


			self.ligne_log.pack()

			self.message3 = Label(self, text="Mot de passe",**argFonfNoir)
			self.message3.pack()

			self.ligne_key.pack()

			self.case.pack(side="top")

			self.bouton_co = Button(self, text="Connectez vous", fg="red", command=self.connexion,background="black")
			self.bouton_co.pack(side="left")
			self.bouton_re = Button(self, text="Inscrivez vous", fg="red", command=self.inscription,background="black")
			self.bouton_re.pack(side="right")

			self.bouton_quitter = Button(self, text="Quitter", command=self.quitter,background="red")
			self.bouton_quitter.pack(side="bottom")
			self.bouton_retour = Button(self, text="Retour", command=self.retour,**argFonfNoir)
			self.bouton_retour.pack(side="bottom")
			self.ligne_log.focus()

	def retour(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.destroy()
		self.fenetre.destroy()
		os.system("python3.8 -m mains.mainDebut")


	def quitter(self) :
		self.serveur.send(b"fin exit(0)")
		self.serveur.close()
		self.destroy()
		self.fenetre.destroy()

	def inscription(self) :
		lancerInterfaceInscription(self.fenetre,self,self.serveur)

class InterfaceUtilisateur(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, serveur,fenetre,joueur, **kwargs):
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
		self.destroy()
		self.fenetre.destroy()

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
		self.destroy()
		self.fenetre.destroy()


	def envoi(self) :
		try :
			essaiInscription(self,self.fenetre,self.var_log.get(),self.var_key.get(),self.var_pseudo.get(),self.serveur)
		except BrokenPipeError :
			print("serveur hors-ligne")
			self.serveur.close()
			self.destroy()
			self.fenetre.destroy()
			os._exit(1)

	def retour(self) :
		retourInterface(self,self.fenetre,self.serveur)

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
		self.destroy()
		self.fenetre.destroy()

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
		frame.ligne_log.config(background = "red")
		frame.ligne_pseudo.config(background = "white")
		frame.ligne_key.config(background = "white")
	elif(retour == "False pseudo") :
		frame.ligne_pseudo.config(background = "red")
		frame.ligne_log.config(background = "white")
		frame.ligne_key.config(background = "white")
	elif(retour == "False encodage") :
		frame.ligne_pseudo.config(background = "white")
		frame.ligne_log.config(background = "red")
		frame.ligne_key.config(background = "red")
	elif(retour == "Done") :
		joueur = Joueur(pseudo)
		with open("../localdata/dataJoueur","wb") as file :
			pickle.dump(joueur,file)
		lancerInterfaceIntermediaire(frame,fenetre,serveur)
	else :
		raise CommunicationError("Message inattendu")

def lancerInterfaceIntermediaire(frame,fenetre,serveur) :
	frame.destroy()
	interface = InterfaceIntermediaire(fenetre,serveur)

	interface.mainloop()
	#interface.destroy()

def retourInterface(frame,fenetre,serveur) :
	frame.destroy()
	interface = InterfaceConnexion(fenetre,serveur)

	interface.mainloop()
	#interface.destroy()


def lancerInterfaceInscription(fenetre,frame,serveur) :
	frame.destroy()
	interface = InterfaceInscription(fenetre,serveur)

	interface.mainloop()
	#interface.destroy()

def lancerInterfaceUtilisateur(frame,serveur,fenetre,joueur) :
	frame.destroy()
	interface = InterfaceUtilisateur(serveur,fenetre,joueur)

	interface.mainloop()
	#interface.destroy()

def lancerInterface(serveur) :
	fenetre = Tk()
	interface = InterfaceConnexion(fenetre,serveur)

	interface.mainloop()
	#fenetre.destroy()