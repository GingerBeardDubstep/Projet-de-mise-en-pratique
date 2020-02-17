#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

from classes.Joueur import *
from fonctions.coteServeur import *
import socket
import select
from fonctions.fonctionsInterface import *

serveur = initialiserServeur()
lecture(serveur)