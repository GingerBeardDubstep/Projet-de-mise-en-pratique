#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
import unittest
from classes.Damier import *
from classes.Bateau import *
from classes.fonctions import *
from classes.exceptions.ExceptionsBateau import *

class TestDamier(unittest.TestCase) :
	def setUp(self) :
		self.dNew = Damier()
		self.dCharge = Damier()
		self.dCharge.changer(0,0,1)
		self.dCharge.changer(19,19,1)
		self.dCharge.changer(10,10,-1)
		self.b = Bateau(5,5,2,"PorteAvion")
		self.p = PorteAvion()

	def testInitDamier(self) :
		d = Damier(self.dCharge)
		self.assertEqual(d.liste[0][0],1)
		self.assertEqual(d.liste[19][19],1)
		self.assertEqual(d.liste[10][10],-1)

	def testPlacer(self) :
		self.dNew.placer("bas","A2",self.b)
		for i in range(0,5) :
			self.assertEqual(self.dNew.getValue(0,1+i),1)
		

		self.dNew.placer("droite","D4",self.p)
		for i in range(0,5) :
			self.assertEqual(self.dNew.getValue(i+3,3),1)

		self.dNew.placer("gauche","R8",self.p)
		for i in range(0,5) :
			self.assertEqual(self.dNew.getValue(17-i,7),1)

		self.dNew.placer("haut","T20",self.p)
		for i in range(0,5) :
			self.assertEqual(self.dNew.getValue(19,19-i),1)
		#print(self.dNew)


		with self.assertRaises(NameError) :
			self.dNew.placer("lol","D4",self.p)

		with self.assertRaises(MauvaisPlacementError) :
			self.dNew.placer("droite","Q1",self.p)

		with self.assertRaises(MauvaisPlacementError) :
			self.dNew.placer("gauche","D1",self.p)

		with self.assertRaises(MauvaisPlacementError) :
			self.dNew.placer("bas","D17",self.p)

		with self.assertRaises(MauvaisPlacementError) :
			self.dNew.placer("haut","D4",self.p)

		with self.assertRaises(PositionError) :
			self.dNew.placer("droite","Q21",self.p)

		with self.assertRaises(PositionError) :
			self.dNew.placer("droite","U20",self.p)

		with self.assertRaises(MauvaisPlacementError) :
			self.dNew.placer("haut","P10",self.p)

	def testTirer(self) :
		self.dNew.placer("bas","A1",self.p)
		self.dNew.tirer("A3")
		self.assertEqual(self.dNew.getValue(0,2),-2)
		self.dNew.tirer("B3")
		self.assertEqual(self.dNew.getValue(1,2),-1)
		with self.assertRaises(ToucheCouleError) :
			self.dNew.tirer("A1")
			self.dNew.tirer("A2")
			self.dNew.tirer("A4")
			self.dNew.tirer("A5")

		with self.assertRaises(PositionError) :
			self.dNew.tirer("A1")

		with self.assertRaises(PositionError) :
			self.dNew.tirer("B3")



	def testChange(self) :
		self.dNew.changer(0,0,1)
		self.dNew.changer(19,19,1)
		self.dNew.changer(10,10,-1)
		self.assertEqual(self.dNew.liste[5][5],0)
		self.assertEqual(self.dNew.liste[0][0],1)
		self.assertEqual(self.dNew.liste[19][19],1)
		self.assertEqual(self.dNew.liste[10][10],-1)
		with self.assertRaises(ValueError):
			self.dNew.changer(20,1,2)
		with self.assertRaises(ValueError):
			self.dNew.changer(-1,1,2)
		with self.assertRaises(ValueError):
			self.dNew.changer(1,20,2)
		with self.assertRaises(ValueError):
			self.dNew.changer(0,-1,2)

	def testGetValue(self) :
		self.assertEqual(self.dCharge.getValue(0,0),1)
		self.assertEqual(self.dCharge.getValue(10,10),-1)
		self.assertEqual(self.dCharge.getValue(19,19),1)
		self.assertEqual(self.dCharge.getValue(1,1),0)

	def testGetCoordFromValue(self) :
		liste1 = self.dCharge.getCoordFromValue(1)
		self.assertTrue("T20" in liste1)
		self.assertTrue("A1" in liste1)
		self.assertFalse("K11" in liste1)

		liste2 = self.dCharge.getCoordFromValue(-1)
		self.assertTrue("K11" in liste2)
		self.assertFalse("A11" in liste2)

		liste0 = self.dCharge.getCoordFromValue(0)
		self.assertEqual(len(liste0),397)

		self.assertTrue(self.dCharge.getCoordFromValue(5)==[])

#unittest.main()