#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "BattleShip V1",
    version = "1.0",
    description = "Jeu de bataille navale",
    executables = [Executable("mainDebut.py")],
)