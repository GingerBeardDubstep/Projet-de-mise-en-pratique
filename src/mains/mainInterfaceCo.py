#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from classes.Joueur import *
from classes.StructureJoueurs import *
from fonctions.fonctionsInterface import *
from interface_graphique.InterfaceDebut import *
import os
try :
	serveur = initialiserClient()
except ConnectionRefusedError :
	print("serveur hors-ligne")
else :
	lancerInterface(serveur)