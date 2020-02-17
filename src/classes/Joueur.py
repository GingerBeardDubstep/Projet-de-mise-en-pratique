#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
import time
class Joueur :
	compt = 0

	def __init__(self,pseudo) :
		self.pseudo = pseudo
		self.niveau = 1
		self.xp = 0
		self.nbVictoires = 0
		self.nbDefaites = 0
		self.nbParties = 0
		self._creation = time.time()

	def addXp(self,xp) :
		self.xp+=xp
		self.verifieLvl()

	def partieGagnee(self) :
		self.nbVictoires+=1
		self.nbParties+=1
		self.addXp(500)

	def partiePerdue(self) :
		self.nbDefaites+=1
		self.nbParties+=1
		self.addXp(0)

	def matchNul(self) :
		self.nbParties+=1
		self.addXp(0)

	def verifieLvl(self) :
		if(self.niveau==1) :
			if(self.xp>=500):
				self.niveau+=1
				self.xp-=500
				self.verifieLvl()
			else :
				pass
		elif(self.niveau==2) :
			if(self.xp>=1500) :
				self.xp-=1500
				self.verifieLvl()
			else :
				pass
		elif(self.niveau==3) :
			if(self.xp>=5000) :
				self.xp-=5000
				self.verifieLvl()
			else :
				pass
		elif(self.niveau==4) :
			if(self.xp>=15000) :
				self.xp-=15000
				self.verifieLvl()
			else :
				pass
		elif(self.niveau==5) :
			if(self.xp>=20000) :
				self.xp-=20000
				self.verifieLvl()
			else :
				pass
		else :
			pass


		