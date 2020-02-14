#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from classes.exceptions.ExceptionsBateau import *
from classes.Damier import *
from classes.fonctions import *
import re




class Bateau :
	identifiant = 1
	def __init__(self,taille,pv,carburant,nom) :
		self.taille=taille
		self._pv = pv
		self.pv = pv
		self.carburant = carburant
		self._carburant = carburant
		self.nom = nom
		self.aFlot = True
		self.id = identifiant
		identifiant+=1
		self.position = []

	def __repr__(slef) :
		return("Le "+nom+" a "+str(pv)+" PV et il lui reste "+str(self.carburant)+" en carburant")

	def __str__(slef) :
		return("Le "+nom+" a "+str(pv)+" PV et il lui reste "+str(self.carburant)+" en carburant")

	def peut_bouger(self) :
		return((self.pv==self._pv) and (self.carburant!=0))

	def placer(self,direction,pos,damier) :
		tst = True
		_damier = Damier(damier)
		if(re.search(r"^[A-T][1-20]$",pos)) :
			absisse, ordonnee = decoder(pos)

			if(direction=="haut") :
				for i in range(0,self.taille) :
					if(ordonnee-i<0) :
						tst = False
						break
				if(tst) :
					for i in range(0,self.taille) :
						self.liste.append((absisse-i,ordonnee))
						damier.changer(absisse-i,ordonnee,1)
			elif(direction=="bas") :
				for i in range(0,self.taille) :
					if(ordonnee+i>=20) :
						tst = False
						break
				if(tst) :
					for i in range(0,self.taille) :
						self.liste.append((absisse+i,ordonnee))
						damier.changer(absisse+i,ordonnee,1)
			elif(direction=="droite") :
				for i in range(0,self.taille) :
					if(absisse+i>=20) :
						tst = False
						break
				if(tst) :
					for i in range(0,self.taille) :
						self.liste.append((absisse,ordonnee+i))
						damier.changer(absisse,ordonnee+i,1)
				else :
					raise MauvaisPlacementError("On ne peut pas placer ce bateau dans ce sens à cet endroit")			

			elif(direction=="gauche") :
				for i in range(0,self.taille) :
					if(absisse-i<0) :
						tst = False
						break
				if(tst) :
					for i in range(0,self.taille) :
						self.liste.append((absisse-i,ordonnee))
						damier.changer(absisse-i,ordonnee,1)
				else :
					raise MauvaisPlacementError("On ne peut pas placer ce bateau dans ce sens à cet endroit")
			else :
				raise NameError(direction+" n'est pas une direction.")
		else :
			raise PositionErrorException(pos+" n'est pas une case du jeu.")



	def avance(self) :
		if(self.peut_bouger()) :
			self.carburant-=1
		else :
			raise NoMovementException("Plus de carburant")  #A définir !

	def ravitaille(self) :
		self.carburant=self._carburant

	def est_touché(self,degats) :
		self.pv-=degats
		if(self.pv<=0) :
			self.pv = 0
			self.est_coule()

	def est_coule(self) :
		self.aFlot = False

class PorteAvion(Bateau) :
	"""Classe porte-avions, elle posséde 2 chasseurs de reconnaissance et a une longueur de 5 cases"""
	def __init__(self) :
		self.__init__(self,5,5,2,"porte-avion")
		self.chasseurs = 2
		self._chasseurs = 2

	def reconaissance(self) :
		if(self.pv!=0) :
			self.chasseurs -= 1
			if(self.chasseur == 0) :
				raise NoWeaponError("Plus de chasseurs")
		else :
			raise EstMortError
	def ravitaille(self) :
		self.ravitaille()
		self.chasseurs = self._chasseurs





class Ravitailleur(Bateau) :
	pass






