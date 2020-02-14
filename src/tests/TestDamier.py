#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*
import unittest
from classes.Damier import *
from classes.fonctions import *
from classes.exceptions.ExceptionsBateau import *

class TestDamier(unittest.TestCase) :
	def setUp(self) :
		self.dNew = Damier()
		self.dCharge = Damier()
		self.dCharge.change(0,0,1)
		self.dCharge.change(19,19,1)
		self.dCharge.change(10,10,-1)

	def testInitDamier(self) :
		d = Damier(self.dCharge)
		self.assertEqual(d.liste[0][0],1)
		self.assertEqual(d.liste[19][19],1)
		self.assertEqual(d.liste[10][10],-1)

	def testChange(self) :
		self.dNew.change(0,0,1)
		self.dNew.change(19,19,1)
		self.dNew.change(10,10,-1)
		self.assertEqual(self.dNew.liste[5][5],0)
		self.assertEqual(self.dNew.liste[0][0],1)
		self.assertEqual(self.dNew.liste[19][19],1)
		self.assertEqual(self.dNew.liste[10][10],-1)
		with self.assertRaises(ValueError):
			self.dNew.change(20,1,2)
		with self.assertRaises(ValueError):
			self.dNew.change(-1,1,2)
		with self.assertRaises(ValueError):
			self.dNew.change(1,20,2)
		with self.assertRaises(ValueError):
			self.dNew.change(0,-1,2)

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

unittest.main()