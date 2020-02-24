#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

import socket
import select
from classes.Joueur import *
from classes.StructureJoueurs import *

def initialiserServeur() :
	serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serveur.bind(('',12800))
	serveur.listen(10)
	return(serveur)

def lecture(serveur) :
	liste_connexions = []
	liste_attente = []
	liste_enJeu = []
	tst = True
	try :
		while(tst) :
			connexions, wlist, xlist = select.select([serveur],(),(),0.05)

			for con in connexions :
				clients, infos = con.accept()

				liste_connexions.append(clients)

			aLire = []
			try :
				aLire, wlist, xlist = select.select(liste_connexions,(),(),0.05)
			except select.error :
				pass
			else :
				for el in aLire :
					msg = el.recv(1024)
					msg = msg.decode()
					if(msg.lower() == "cherche") :							
						liste_attente.append(el)
						el.send(b"pas encore")
					if(msg.lower() == "attente") :
						tst1=False
						for el1,el2 in liste_enJeu :
							if((el is el1) or (el is el2)) :
								el.send(b"trouve")
								tst=True
						if(tst1) :
							pass
						else :
							if(len(liste_attente)>1) :
								if(el is liste_attente[0]) :
									liste_enJeu.append((el,liste_attente[1]))
									liste_attente.remove(liste_attente[1])
									liste_attente.remove(el)
								else :
									liste_enJeu.append((el,liste_attente[0]))
									liste_attente.remove(liste_attente[0])
									liste_attente.remove(el)
								el.send(b"trouve")
							else :
								el.send(b"pas encore")						

					if(msg.lower() == "actualiser profil") :
						structure = StructureJoueurs()
						try :
							structure.importStructure()
						except :
							structure = StructureJoueurs()
						login = el.recv(1024).decode()
						mdp = el.recv(1024).decode()
						joueurActuel = el.recv(1024)
						joueurActuel = pickle.loads(joueurActuel)
						try :
							structure.actualiserJoueur(joueurActuel,login,mdp)
						except NoPlayerFoundException :
							el.send(b"False")
						except NoActualException :
							el.send(b"False")
						else :
							el.send(b"Done")
					if(msg.lower() == "tentative connexion") :
						structure = StructureJoueurs()
						try :
							structure.importStructure()
						except :
							structure = StructureJoueurs()
						login = el.recv(1024).decode()
						mdp = el.recv(1024).decode()
						joueur = None
						try :
							joueur = structure.getJoueur(login,mdp)
						except NoPlayerFoundException :
							el.send(b"False")
						else :
							joueur = pickle.dumps(joueur)
							el.send(joueur)
					elif(msg.lower()=="tentative inscription") :
						structure = StructureJoueurs()
						structure.importStructure()
						login = el.recv(1024).decode()
						mdp = el.recv(1024).decode()
						pseudo = el.recv(1024).decode()
						try :
							structure.ajouterJoueur(Joueur(pseudo),login,mdp)
						except LoginExistantException :
							el.send(b"False login")
						except PseudoExistantException :
							el.send(b"False pseudo")
						except HashException :
							el.send(b"False encodage")
						else :
							structure.editStructure()
							el.send(b"Done")

					elif(msg.lower()=="fin exit(0)") :
						el.close()
						liste_connexions.remove(el)
						break
					elif(msg.lower()=="fermeture reseau principal") :
						for el in liste_connexions :
							try :
								el.send(b"coupure reseau")
							except BrokenPipeError :
								pass
							el.close()
							serveur.close()
							tst=False


	except KeyboardInterrupt :
		for el in liste_connexions :
			el.send(b"fin exit(0)")
			el.close()
		serveur.close()
		print("WTF?")
		raise KeyboardInterrupt
