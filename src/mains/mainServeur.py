#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from classes.Joueur import *
from fonctions.coteServeur import *
import socket
import select

serveur = initialiserServeur()
lecture(serveur)