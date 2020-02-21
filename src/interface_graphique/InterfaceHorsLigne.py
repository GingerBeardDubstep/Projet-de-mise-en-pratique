#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from tkinter import *
import pickle
from classes.Partie import *
#from fonctions.fonctionsDamier import *
import socket
import os
import time
from fonctions.fonctionsInterface import *

class InterfaceJeuHL(Frame) :
	def __init__(self, fenetre,joueur, **kwargs):
		fenetre.geometry("800x800")
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.pack(fill=BOTH)
		self.fenetre = fenetre
		self.joueur = joueur
		self.aPlace = False
		self.IA = Joueur("Ordinateur")
		self.d1 = Damier()
		self.d2 = Damier()
		self.message = Label(self,text="Etape 1 : Placez vos bateaux")
		self.message.grid(row=0,column=15)
		self.partie = Partie(self.joueur,self.d1,self.IA,self.d2)
		self.partie.placerIA()
		self.partie.tour[0] = self.joueur
		self.d2 = self.partie.grille2
		self.grillePerso = GrillePlacement(self,self.d1)
		self.grilleTir = GrilleTir(self,self.d2)
		self.message.grid(row=1,column=15)
		self.grillePerso.grid(row=2,column=15)
		self.grilleTir.grid(row=3,column=15)
		self.valider = Button(self,text="Valider",fg="white",bg="green",command=self.valider)
		self.valider.grid(row=4,column=15)
		#self.partie = Partie(self.joueur,Damier(),self.IA,Damier())
		#self.boutonDepart = Button(self,text="Lancer la partie",bg="red",fg="white",state = "disabled",command=self.lancerPartie)
		#self.boutonPlacer = Button(self,text="Placez vos bateaux",bg="green",fg="white",state="enabled")
		
	def valider(self) :
		if(self.grillePerso.remplie()) :
			self.grillePerso.disableGrille()
			self.grilleTir.enableGrille()
			self.message.config(text="Etape 2 : Jouez")

class GrillePlacement(Frame) :
	def __init__(self,interface,damier,**kwargs) :
		Frame.__init__(self,interface,width = 330, height = 390, **kwargs)
		self.etat = "enabled"
		self.valider = Button(self,text="Valider",fg="white",bg="red",command=self.valider)
		self.listeCases = []
		self.interface = interface
		self.damier = damier
		listeAbs = ["A","B","C","D","E","F","G","H","I","J"]
		listeOrd = ["1","2","3","4","5","6","7","8","9","10"]
		for i in range(10):
			Label(self,text=listeAbs[i],bg="white").grid(row=1,column=i+1+10)
			Label(self,text=listeAbs[i],bg="white").grid(row=i+2,column=0+10)
			for j in range(10):
				valeur = IntVar()
				jb = JBCheckbutton(self, variable=valeur,bg="white",command=self.checkCase)
				jb.grid(row=j+2, column=i+1+10)
				jb.coordonnee = encoder(i,j)
				jb.deselect()
				self.listeCases.append((jb,valeur))

		self.val_bateau = StringVar()
		self.pA = Radiobutton(self,variable=self.val_bateau,text="Porte-Avion(5)",value="pA")
		self.c = Radiobutton(self,variable=self.val_bateau,text="Croiseur(4)",value="c")
		self.cT = Radiobutton(self,variable=self.val_bateau,text="Contre-Torpilleur(3)",value="cT")
		self.sM = Radiobutton(self,variable=self.val_bateau,text="Sous-Marin(3)",value="sM")
		self.t = Radiobutton(self,variable=self.val_bateau,text="Torpilleur(2)",value="t")

		self.dejaPlace = []

		self.pA.grid(row=12,column=6,columnspan=10)
		self.c.grid(row=12,column=14,columnspan=10)
		self.cT.grid(row=12,column=22,columnspan=10)
		self.sM.grid(row=13,column=9,columnspan=10)
		self.t.grid(row=13,column=16,columnspan=10)
		self.t.deselect()

		self.valider.grid(row=14,column=15,columnspan=10)

	def checkCase(self) :
		for bouton,val in self.listeCases :
			if(val.get()==1) :
				bouton.config(bg="grey")

	def remplie(self) :
		tst = True
		if(self.pA.cget("state")=="normal") :
			tst=False
		elif(self.c.cget("state")=="normal") :
			tst=False
		elif(self.cT.cget("state")=="normal") :
			tst=False
		elif(self.sM.cget("state")=="normal") :
			tst=False
		elif(self.t.cget("state")=="normal") :
			tst=False
		return(tst)

	def valider(self) :
		if(self.val_bateau.get()=="pA" and "pA" not in self.dejaPlace) :
			tst = False
			xmin=-1
			ymin=-1
			direc = ""
			pos = []
			but = []
			for bouton,val in self.listeCases :
				if(val.get()==1) :
					val.set(0)
					bouton.config(bg="white")
					pos.append(bouton.getCoord())
					but.append(bouton)
			if(len(pos)==5) :
				y1, x1 = decoder(pos[0])
				y2, x2 = decoder(pos[1])
				y3, x3 = decoder(pos[2])
				y4, x4 = decoder(pos[3])
				y5, x5 = decoder(pos[4])
				if(x1==x2==x3==x4==x5) :
					if(abs(y1-y2)<5 and abs(y2-y3)<5 and abs(y1-y3)<5 and abs(y1-y4)<5 and abs(y2-y4)<5 and abs(y3-y4)<5 and abs(y1-y5)<5 and abs(y2-y5)<5 and abs(y3-y5)<5 and abs(y4-y5)<5) :
						tst = True
						ymin = min(y1,y2,y3,y4,y5)
						xmin = x1
						direc = "bas"
				elif(y1==y2==y3==y4==y4) :
					if(abs(x1-x2)<5 and abs(x2-x3)<5 and abs(x1-x3)<5 and abs(x1-x4)<5 and abs(x2-x4)<5 and abs(x3-x4)<5 and abs(x1-x5)<5 and abs(x2-x5)<5 and abs(x3-x5)<5 and abs(x4-x5)<5) :
						tst = True
						xmin = min(x1,x2,x3,x4,x5)
						ymin = y1
						direc = "droite"
			if(tst) :
				self.damier.placer(direc,encoder(xmin,ymin),PorteAvion())
				self.dejaPlace.append("pA")
				for b in but :
					b.config(state="disabled",bg="green")
					self.pA.deselect()
					self.pA.config(state="disabled")
					
			else :
				self.reinit()
		elif(self.val_bateau.get()=="c" and "c" not in self.dejaPlace) :
			tst = False
			xmin=-1
			ymin=-1
			direc = ""
			pos = []
			but = []
			for bouton,val in self.listeCases :
				if(val.get()==1) :
					val.set(0)
					bouton.config(bg="white")
					pos.append(bouton.getCoord())
					but.append(bouton)
			if(len(pos)==4) :
				y1, x1 = decoder(pos[0])
				y2, x2 = decoder(pos[1])
				y3, x3 = decoder(pos[2])
				y4, x4 = decoder(pos[3])
				if(x1==x2==x3==x4) :
					if(abs(y1-y2)<4 and abs(y2-y3)<4 and abs(y1-y3)<4 and abs(y1-y4)<4 and abs(y2-y4)<4 and abs(y3-y4)<4) :
						tst = True
						ymin = min(y1,y2,y3,y4)
						xmin = x1
						direc = "bas"
				elif(y1==y2==y3==y4) :
					if(abs(x1-x2)<4 and abs(x2-x3)<4 and abs(x1-x3)<4 and abs(x1-x4)<4 and abs(x2-x4)<4 and abs(x3-x4)<4) :
						tst = True
						xmin = min(x1,x2,x3,x4)
						ymin = y1
						direc = "droite"
			if(tst) :
				self.damier.placer(direc,encoder(xmin,ymin),Croiseur())
				self.dejaPlace.append("c")
				for b in but :
					b.config(state="disabled",bg="green")
					self.c.deselect()
					self.c.config(state="disabled")
					
			else :
				self.reinit()
		elif(self.val_bateau.get()=="cT" and "cT" not in self.dejaPlace) :
			tst = False
			xmin=-1
			ymin=-1
			direc = ""
			pos = []
			but = []
			for bouton,val in self.listeCases :
				if(val.get()==1) :
					val.set(0)
					bouton.config(bg="white")
					pos.append(bouton.getCoord())
					but.append(bouton)
			if(len(pos)==3) :
				y1, x1 = decoder(pos[0])
				y2, x2 = decoder(pos[1])
				y3, x3 = decoder(pos[2])
				if(x1==x2==x3) :
					if(abs(y1-y2)<3 and abs(y2-y3)<3 and abs(y1-y3)<3) :
						tst = True
						ymin = min(y1,y2,y3)
						xmin = x1
						direc = "bas"
				elif(y1==y2==y3) :
					if(abs(x1-x2)<3 and abs(x2-x3)<3 and abs(x1-x3)<3) :
						tst = True
						xmin = min(x1,x2,x3)
						ymin = y1
						direc = "droite"
			if(tst) :
				self.damier.placer(direc,encoder(xmin,ymin),ContreTorpilleur())
				self.dejaPlace.append("cT")
				for b in but :
					b.config(state="disabled",bg="green")
					self.cT.deselect()
					self.cT.config(state="disabled")
					
			else :
				self.reinit()
		elif(self.val_bateau.get()=="sM" and "sM" not in self.dejaPlace) :
			tst = False
			xmin=-1
			ymin=-1
			direc = ""
			pos = []
			but = []
			for bouton,val in self.listeCases :
				if(val.get()==1) :
					val.set(0)
					bouton.config(bg="white")
					pos.append(bouton.getCoord())
					but.append(bouton)
			if(len(pos)==3) :
				y1, x1 = decoder(pos[0])
				y2, x2 = decoder(pos[1])
				y3, x3 = decoder(pos[2])
				if(x1==x2==x3) :
					if(abs(y1-y2)<3 and abs(y2-y3)<3 and abs(y1-y3)<3) :
						tst = True
						ymin = min(y1,y2,y3)
						xmin = x1
						direc = "bas"
				elif(y1==y2==y3) :
					if(abs(x1-x2)<3 and abs(x2-x3)<3 and abs(x1-x3)<3) :
						tst = True
						xmin = min(x1,x2,x3)
						ymin = y1
						direc = "droite"
			if(tst) :
				self.dejaPlace.append("sM")
				self.damier.placer(direc,encoder(xmin,ymin),SousMarin())
				for b in but :
					b.config(state="disabled",bg="green")
					self.sM.deselect()
					self.sM.config(state="disabled")
					
			else :
				self.reinit()
		elif(self.val_bateau.get()=="t" and "t" not in self.dejaPlace) :
			tst = False
			xmin=-1
			ymin=-1
			direc = ""
			pos = []
			but = []
			for bouton,val in self.listeCases :
				if(val.get()==1) :
					val.set(0)
					bouton.config(bg="white")
					pos.append(bouton.getCoord())
					but.append(bouton)
			if(len(pos)==2) :
				y1, x1 = decoder(pos[0])
				y2, x2 = decoder(pos[1])
				if(x1==x2 and (y1==y2-1 or y1==y2+1)) :
					tst=True
					ymin = min(y1,y2)
					xmin=x1
					direc = "bas"
				elif(y1==y2 and (x1==x2+1 or x1==x2-1)) :
					tst=True
					xmin=min(x1,x2)
					ymin=y1
					direc = "droite"
			if(tst) :
				self.dejaPlace.append("t")
				self.damier.placer(direc,encoder(xmin,ymin),Torpilleur())
				for b in but :
					b.config(state="disabled",bg="green")
					self.t.deselect()
					self.t.config(state="disabled")
					
			else :
				self.reinit()
	def reinit(self) :
		for jb,val in self.listeCases :
			if(jb.cget("state")!="disabled") :
				val.set(0)

	def disableGrille(self) :
		for bouton,val in self.listeCases :
			bouton.config(state="disabled")
			val.set(0)
		


class JBCheckbutton(Checkbutton) :
	def __init__(self,fenetre,**kwargs) :
		Checkbutton.__init__(self,master=fenetre,**kwargs)
		self.coordonnee = "Z11"

	def getCoord(self) :
		return(self.coordonnee)

class GrilleTir(Frame) :
	def __init__(self,interface,damier,**kwargs) :
		Frame.__init__(self,interface,width = 330,height = 390, **kwargs)
		self.etat = "disabled"
		self.listeBateau = damier.listeBateau
		self.interface=interface
		self.damier = damier
		listeAbs = ["A","B","C","D","E","F","G","H","I","J"]
		listeOrd = ["1","2","3","4","5","6","7","8","9","10"]
		self.listeRadio = []

		for i in range(10):
			Label(self,text=listeAbs[i],bg="white").grid(column=i+1,row=0)
			Label(self,text=listeOrd[i],bg="white").grid(column=0,row=i+1)
		self.valeur=StringVar()
		for i in range(10):
			for j in range(10):
				rb = Radiobutton(self, variable=self.valeur, value=encoder(i,j),cursor="target")
				if(self.damier.getValue(i,j)==-1) :
					rb.config(bg="grey",fg="red",state="disabled")
				elif(self.damier.getValue(i,j)==-2) :
					rb.config(bg="red",fg="white",state="disabled")
				elif(self.damier.getValue(i,j)==-3) :
					rb.config(bg="green",fg="red",state="disabled")
				else :
					rb.config(bg="white",fg="black",state="disabled")
				rb.grid(row=j+1, column=i+1)
				rb.deselect()
				self.listeRadio.append(rb)

		self.bouton_tirer = Button(self,text="Tirer",bg="red",fg="white",command=self.tirer,state="disabled",cursor="target")
		self.bouton_tirer.grid(column=3,row=12,columnspan=5)
		self.bouton_secours = Button(self,text="DEBLOQUE!",bg="red",fg="white",command=self.enableGrille)
		self.bouton_secours.grid(column=3,row=13,columnspan=5)

	def enableGrille(self) :
		self.etat="enabled"
		for rb in self.listeRadio :
			if(rb.cget("bg")=="white") :
				rb.config(state="normal")
				rb.select()
		self.bouton_tirer.config(state="normal")

	def tirer(self) :
		try :
			self.damier.tirer(self.valeur.get())
		except ToucheException :
			for rb in self.listeRadio :
				if(rb.cget("value")==self.valeur.get()) :
					rb.config(bg="red",state="disabled")
				rb.config(state="disabled")
		except ToucheCouleException :
			position = []
			for bat in self.listeBateau :
				#print(bat.getPosition)
				if(self.valeur.get() in bat.getPosition()) :
					position = bat.getPosition()
			for coord in position :
				for rb in self.listeRadio :
					if(rb.cget("value")==coord) :
						rb.config(bg="green",state="disabled")
					rb.config(state="disabled")
		else :
			for rb in self.listeRadio :
				if(rb.cget("value")==self.valeur.get()) :
					rb.config(bg="grey",state="disabled")
				rb.config(state="disabled")
		self.bouton_tirer.config(state="disabled")
		self.etat = "disabled"
			
			
class InterfaceHorsLigne(Frame) :
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.joueur = Joueur("__localhost__")
		try :
			file=open("../localdata/dataJoueur","rb")
		except FileNotFoundError :
			self.joueur = Joueur("__localhost__")
			with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur,file)
		else :
			self.joueur = pickle.load(file)
		finally :
			self.pack(fill=BOTH)
			self.reinitTot()

		
		# Création de nos widgets
		

#3A37666FACCADE7D47AC6C6F34

	def jouer(self) :
		self.destroy()
		instance = InterfaceJeuHL(self.fenetre,self.joueur)
		


	def reinitTot(self) :
		
		self.message = Label(self, text="Bienvenue "+self.joueur.pseudo)
		self.message.pack(side="top")


		self.bouton_co = Button(self, text="Lancez une partie !", fg="white",background="blue", command=self.lancerJeu)
		self.bouton_co.pack()
		self.bouton_quitter = Button(self, text="Quitter", command=self.quitter)
		self.bouton_quitter.pack(side="bottom")

	def quitter(self) :
		"""with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur)"""
		self.destroy()
		self.fenetre.destroy()

	def lancerJeu(self) :
		if(self.joueur.pseudo=="__localhost__") :
			self.destroy()
			interface = InterfaceQuestion(self.fenetre)
			interface.mainloop()
		else :
			self.destroy()
			self.fenetre.destroy()
			fenetre = Tk()
			fenetre.geometry("800x800")
			instance = InterfaceJeuHL(fenetre,self.joueur)
			instance.mainloop()


class InterfaceQuestion(Frame) :
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		self.fenetre = fenetre
		Frame.__init__(self, fenetre, width=(7680/2), height=(5760/2), **kwargs)
		self.pack(fill=BOTH)
		self.reinitTot()
		# Création de nos widgets

	def reinitTot(self) :
		self.message = Label(self, text="Pour sauvegarder votre progression hors-ligne, il faut vous inscrire.")
		self.message.pack(side="top")

		self.bouton_co = Button(self, text="Inscrivez-vous !",fg="green", command=self.lancerInscription)
		self.bouton_co.pack(side="left")
		self.bouton_re = Button(self, text="Jouer sans sauvegarde", fg="red", command=self.lancerJeuHL)
		self.bouton_re.pack(side="right")
		self.bouton_quitter = Button(self, text="Quitter", command=self.quitter)
		self.bouton_quitter.pack(side="bottom")

	def quitter(self) :
		"""with open("../localdata/dataJoueur","wb") as file :
				pickle.dump(self.joueur)"""
		self.destroy()
		self.fenetre.destroy()

	def lancerInscription(self) :
		self.destroy()
		try :
			serveur = initialiserClient()
		except ConnectionRefusedError :
			self.destroy()
			self.fenetre.destroy()
			os.system("python3.8 -m mains.mainDebut")
			print("serveur hors-ligne")
			os._exit(1)
		else :
			instance = InterfaceInscription(self.fenetre,serveur)
			instance.mainloop()

		"""os.system("python3.8 -m mains.mainInterfaceInscr")
		os._exit(0)"""

	def lancerJeuHL(self) :
		self.destroy()
		self.fenetre.destroy()
		fenetre = Tk()
		fenetre.geometry("800x800")
		instance = InterfaceJeuHL(fenetre,Joueur("__localhost__"))
		instance.mainloop()


