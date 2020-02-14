class NoMovementException(Exception) :
	def __init__(self,message) :
		print(message)
		self.message=message

	def __str__(self) :
		return(self.message)

class NoWeaponError(Exception) :
	def __init__(self,message) :
		print(message)
		self.message=message

	def __str__(self) :
		return(self.message)

class PositionError(Exception) :
	def __init__(self,message) :
		print(message)
		self.message=message

	def __str__(self) :
		return(self.message)