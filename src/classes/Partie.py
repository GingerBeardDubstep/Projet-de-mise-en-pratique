#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from classes.Joueur import *
from classes.Damier import *
from classes.exceptions.ExceptionsBateau import *
import random

class Partie :

	def __init__(self,joueur1,damier1,joueur2,damier2) :
		self.enCours = True
		self.joueur1=joueur1
		self.joueur2=joueur2
		self.tour = [random.choice([self.joueur2,self.joueur1])]
		self.grille1 = damier1
		self.grilleAdverse1 = Damier()
		self.grille2 = damier2
		self.grilleAdverse2 = Damier()

	def tirer(self,pos) :
		if(self.tour[0]==self.joueur1) :
			try :
				self.grille2.tirer(pos)
			except ToucheCouleException :
				ordonne, absisse = pos.decode()
				self.grilleAdverse1.changer(absisse,ordonnee,-3)
				raise ToucheCouleException("")
			except ToucheException :
				ordonne, absisse = pos.decode()
				self.grilleAdverse1.changer(absisse,ordonnee,-2)
				raise ToucheException("")
			else :
				self.grilleAdverse1.tirer(pos)
				raise NoHarmException("Dans l'eau.")

		else :
			try :
				self.grille1.tirer(pos)
			except ToucheCouleException :
				ordonne, absisse = pos.decode()
				self.grilleAdverse2.changer(absisse,ordonnee,-3)
				raise ToucheCouleException("")
			except ToucheException :
				ordonne, absisse = pos.decode()
				self.grilleAdverse2.changer(absisse,ordonnee,-2)
				raise ToucheException("")
			else :
				self.grilleAdverse2.tirer(pos)
				raise NoHarmException("Dans l'eau.")

	def tourTermine(self) :
		if(self.tour[0]==self.joueur1) :
			self.tour = [self.joueur2]
		else :
			self.tour = [self.joueur1]

	def testFin(self) :
		self.enCours = self.grille1.estVide() or self.grille2.estVide()
		if(self.enCours) :
			raise FinDuJeuException("Le jeu est fini.")

