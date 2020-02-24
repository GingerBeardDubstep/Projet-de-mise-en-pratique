#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from classes.exceptions.ExceptionsStock import *
from classes.Joueur import *
import hashlib
import pickle
class StructureJoueurs :

	def __init__(self) :
		self.dicoJoueurs = dict()
		self.listeLogin = []

	def ajouterJoueur(self,joueur,login,mdp) :
		for j in self.dicoJoueurs.values() :
			if(j.pseudo==joueur.pseudo) :
				raise PseudoExistantException("Ce pseudo existe déjà")
		for l in self.listeLogin :
			if(l==login) :
				raise LoginExistantException("Ce login existe déjà")
		self.listeLogin.append(login)
		_temp = mdp+login+mdp
		clef = hashlib.sha1(_temp.encode()).hexdigest()
		if(clef in self.dicoJoueurs.keys()) :
			raise HashException("Cet id existe déjà")
		else :
			self.dicoJoueurs[clef] = joueur

	def actualiserJoueur(self,joueur,login,mdp) :
		clef = hashlib.sha1((mdp+login+mdp).encode()).hexdigest()
		if(clef in self.dicoJoueurs.keys()) :
			if(self.dicoJoueurs[clef].niveau<joueur.niveau) :
				self.dicoJoueurs[clef]=joueur
				self.editStructure()
			elif(self.dicoJoueurs[clef].niveau==joueur.niveau) :
				if(self.dicoJoueurs[clef].xp<joueur.xp) :
					self.dicoJoueurs[clef]=joueur
					self.editStructure()
				else :
					raise NoActualException("Pas d'actualisation")
			else :
				raise NoActualException("pas d'actualisation")
		else :
			raise NoPlayerFoundException("Login ou mot de passe incorrrect")

	def getJoueur(self,login,mdp) :
		_temp = mdp+login+mdp
		clef = hashlib.sha1(_temp.encode()).hexdigest()
		tst = False
		for cle in self.dicoJoueurs.keys() :
			if(clef==cle) :
				return(self.dicoJoueurs[cle])
		raise NoPlayerFoundException("Login ou mot de passe incorect")

	def editStructure(self) :
		file = open("../serveurdata/data","wb")
		pickler = pickle.Pickler(file)
		pickler.dump(self)
		file.close()

	def importStructure(self) :
		try :
			file=open("../serveurdata/data","rb")
		except FileNotFoundError :
			self.dicoJoueurs = dict()
			self.listeLogin =[]
		else :
			depickler = pickle.Unpickler(file)
			_temp = depickler.load()
			self.dicoJoueurs = dict(_temp.dicoJoueurs)
			self.listeLogin = list(_temp.listeLogin)
			file.close()
		
