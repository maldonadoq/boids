import numpy as np

class Boid:
	def __init__(self, position=np.zeros(2), velocity=np.zeros(2), acceleration=np.zeros(2)):
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration

	def __repr__(self):
		return '({} : {})'.format(self.position, self.velocity)