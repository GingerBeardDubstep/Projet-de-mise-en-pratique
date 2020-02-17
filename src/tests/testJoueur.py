import unittest
from classes.Joueur import *

class TestBateau(unittest.TestCase) :
	def setUp(self) :
		self.joueur = Joueur("R2d2")

	def testMatch(self) :
		self.joueur.partieGagnee()
		self.assertEqual(self.joueur.niveau,2)
		self.assertEqual(self.joueur.xp,0)

		self.joueur.partieGagnee()
		self.joueur.partiePerdue()
		self.assertEqual(self.joueur.niveau,2)
		self.assertEqual(self.joueur.xp,500)
		self.assertEqual(self.joueur.nbParties,3)