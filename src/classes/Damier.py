#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from classes.fonctions import *
class Damier() :
	def __init__(self,*args) :
		self.liste = []
		if(not args) :
			for i in range(0,20) :
				liste1=[]
				for j in range(0,20) :
					liste1.append(0)
				self.liste.append(list(liste1))
		else :
			for el in args :
				self.liste = list(el.liste)
				break

	def __repr__(self) :
		string = "[\n"
		for i in self.liste :
			string+=str(i)+"\n"
		string+= "]"
		return(string)

	def __str__(self) :
		string = "["
		for i in self.liste :
			string+=str(i)+"\n"
		string+= "]"
		return(string)

	def change(self,absisse,ordonnee,val) :
		if(absisse<0 or absisse>19 or ordonnee<0 or ordonnee>19) :
			raise ValueError
		else :
			self.liste[absisse][ordonnee] = val

	def getValue(self,absisse,ordonnee) :
		if(absisse<0 or absisse>19 or ordonnee<0 or ordonnee>19) :
			raise ValueError
			return(None)
		else :
			return(self.liste[absisse][ordonnee])

	def getCoordFromValue(self,val) :
		liste = []
		cpt1 = 0
		cpt2 = 0
		for i in self.liste :
			cpt2 = 0
			for j in i :
				if(val==j) :
					liste.append(encoder(cpt1,cpt2))
				cpt2+=1
			cpt1+=1
		return(liste)
