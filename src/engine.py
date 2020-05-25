import numpy as np
import random as rn

from .boid import Boid

sep = 25

class Engine:
	def __init__(self, width=500, heigth=500):
		self.width = width
		self.heigth = heigth
		self.target = np.array([rn.randint(0, self.width), rn.randint(0, self.heigth)])

	def initialization(self, numbers):
		self.boids = []
		for i in range(numbers):
			self.boids.append(Boid(	np.array([rn.randint(0, self.width), rn.randint(0, self.heigth)]),
									np.array([1,1])))

	def update(self):
		tmp = self.boids

		for i, boid in enumerate(tmp):
			if np.linalg.norm(boid.position-self.target) < 100:
				self.target = np.array([rn.randint(0, self.width), rn.randint(0, self.heigth)])
				
			v1 = self.cohesion(i, boid)
			v2 = self.alignment(i, boid)
			v3 = self.separation(i, boid)
			goal = self.goal(boid)

			boid.velocity = v1 + v2 + v3 + goal
			boid.position = boid.position + boid.velocity

			boid.position[0] %= self.width
			boid.position[1] %= self.heigth

	def cohesion(self, iT, boidT):
		c = np.zeros(2)

		total = 0
		for i, boid in  enumerate(self.boids):
			if(i != iT):				
				total += 1
				c = c + boid.position
		
		c = c / total

		return (c - boidT.position) / 100

	def alignment(self,pos, boidT):
		v = np.zeros(2)
		total = 0

		for i,boid in enumerate(self.boids):
			if (i != pos):
				v = v + boid.velocity
				total += 1

		v = v / total
		return (v - boidT.velocity) / 20

	def separation(self, pos, boidT):
		s = np.zeros(2)

		total = 0
		for i,boid in enumerate(self.boids):
			if (i != pos):
				if(np.linalg.norm(boid.position - boidT.position) < 30):
					s = s - (boid.position - boidT.position)
					total += 1
		
		#if(total != 0):
		#	s = s / total
		return s / 10

	def goal(self, boidT):
		return (self.target - boidT.position) / 50

	def print(self):
		for boid in self.boids:
			print(boid)
		print()