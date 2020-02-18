#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
from classes.exceptions.ExceptionsBateau import *
def encoder(x,y) :
	"""Renvoie un string correspondant à la case : encode(0,3) renvoie "A4" """
	_y=str(y+1)
	_x=""
	if(x==0) :
		_x="A"
	elif(x==1) :
		_x="B"
	elif(x==2) :
		_x="C"
	elif(x==3) :
		_x="D"
	elif(x==4) :
		_x="E"
	elif(x==5) :
		_x="F"
	elif(x==6) :
		_x="G"
	elif(x==7) :
		_x="H"
	elif(x==8) :
		_x="I"
	elif(x==9) :
		_x="J"
	elif(x==10) :
		_x="K"
	elif(x==11) :
		_x="L"
	elif(x==12) :
		_x="M"
	elif(x==13) :
		_x="N"
	elif(x==14) :
		_x="O"
	elif(x==15) :
		_x="P"
	elif(x==16) :
		_x="Q"
	elif(x==17) :
		_x="R"
	elif(x==18) :
		_x="S"
	elif(x==19) :
		_x="T"
	else :
		raise PositionError("position impossible a")
		return(None,None)
	if(y+1>20) :
		raise PositionError("position impossible b")
		return(None,None)
	else :
		return(_x+_y)

def decoder(pos) :
	"""Renvoie un couple d'abscisse ordonnee correspondant à la case : decode("A4") renvoie 0,3 """
	_x=pos[0]
	x=-1
	_y = pos[1:]
	y=int(pos[1:])-1
	if(_x=="A") :
		x=0
	elif(_x=="B") :
		x=1
	elif(_x=="C") :
		x=2
	elif(_x=="D") :
		x=3
	elif(_x=="E") :
		x=4
	elif(_x=="F") :
		x=5
	elif(_x=="G") :
		x=6
	elif(_x=="H") :
		x=7
	elif(_x=="I") :
		x=8
	elif(_x=="J") :
		x=9
	elif(_x=="K") :
		x=10
	elif(_x=="L") :
		x=11
	elif(_x=="M") :
		x=12
	elif(_x=="N") :
		x=13
	elif(_x=="O") :
		x=14
	elif(_x=="P") :
		x=15
	elif(_x=="Q") :
		x=16
	elif(_x=="R") :
		x=17
	elif(_x=="S") :
		x=18
	elif(_x=="T") :
		x=19
	else :
		raise PositionError(_x+_y+" n'existe pas")
		return(None,None)
	if(y>=20) :
		raise PositionError(_x+_y+" n'existe pas")
		return(None,None)
	else :
		return(y,x)