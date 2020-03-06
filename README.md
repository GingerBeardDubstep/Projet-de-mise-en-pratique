# Projet-de-mise-en-pratique
Projet transversal des connaissances accumulées

#Phase 1 : Définition :
Jeu de type bataille navale :
								Un serveur pour mettre les joueurs en relation 
								Un moyen de sauvegarder les données utilisateurs
								Pouvoir se connecter avec un identifiant et un mot de passe
								Etre mis en relation avec d'autres joueurs
								Systeme de niveaux
								Interface Graphique
								Systeme d'armes, de niveaux, de pouvoirs, de surprises aléatoires, ...

Prévision : 30h

Gantt : 
	implémenter les classes (Bateau,Croiseur,Joueur,...) : 2h Done
	implémenter la fenêtre de connexion : 1h Done
	implementer les fonctions d'enregistrement et de connexion : 1h Done
	établir les règles du jeu : 3h Done
	implémennter le script à exécuter pour faire une partie : 3h Done
	implémenter la connexion serveur/clients : 2h Done
	implémenter le programme client : 2h Done
	implémenter l'interface post connexion du jeu : 2h Done
	implémenter l'interface de jeu : 5h Done
	implémenter un main : 3h Done
	créer des exécutables linux / Windows : 3h Done (Linux)


Méthode : Test Driven

#Phase 2 : Classes

#Phase 3 : Connexion

#Phase 4 : La partie + décision des fonctionalités

#Phase 5 :Serveur/Clients

#Phase 6 : Interface

#Phase 7 : Main

#Phase 8 : Exportation du projet

#ToDo : {Clases, Connexion, Partie + fonctionnalités, Serveur/Client, Interface, Main, Exportation du projet}

#Done : {ALL}

#Indications de fonctionnement :
	--Pour le mode Hors-Ligne :
		-Allez dans le dossier BattleShipV1 et exécutez mainDebut
		-Laissez-vous guider par l'interface (Je vous conseille de rapidement passer en mode réseau pour sauvegarder votre avancée)

	--Pour le mode réseau :
		-Dans le répertoire src, écrivez en ligne de commande : python3.8 -m mains.mainServeur
		-Lancez le logiciel comme en mode Hors-Ligne.
		-Vous avez accès au mode en réseau

	--Pour éteindre le serveur : 
		-Dans src lancez : ./fonctions/fermetureServeur.py

