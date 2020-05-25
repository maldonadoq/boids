import numpy as np
import random as rn

from .boid import Boid

sep = 25

class Engine:
	def __init__(self, width=500, heigth=500):
		self.width = width
		self.heigth = heigth
		self.target = np.zeros(2)

	def initialization(self, numbers):
		self.boids = []
		for i in range(numbers):
			self.boids.append(Boid(	np.array([rn.randint(0, self.width), rn.randint(0, self.heigth)]),
									np.array([1,1])))

	def update(self):
		tmp = self.boids

		for i, boid in enumerate(tmp):
			if np.linalg.norm(boid.position-self.target) < 50:
				self.target = np.array([rn.randint(0, self.width), rn.randint(0, self.heigth)])
				
			v1 = self.cohesion(i, boid)
			v2 = self.alignment(i, boid)
			goal = self.goal(boid)

			boid.velocity = v1 + v2 + goal
			boid.position = boid.position + boid.velocity

			boid.position[0] %= self.width
			boid.position[1] %= self.heigth

	def cohesion(self, iT, boidT):
		c = np.zeros(2)
		total = 0

		for i, boid in  enumerate(self.boids):
			if(i != iT):
				if(np.linalg.norm(boid.position - boidT.position) < 4*sep):
					total += 1
					c = c + boid.position
		
		if(total > 0):
			c = c / total

		return (c - boidT.position) / 100

	def alignment(self,pos, boidT):
		v = np.zeros(2)
		total = 0

		for i,boid in enumerate(self.boids):
			if (i != pos):
				v = v + boidT.velocity
				total +=1

		v = v / total
		return (v - boidT.velocity) / 8

	def goal(self, boidT):
		return (self.target - boidT.position) / 100

	def print(self):
		for boid in self.boids:
			print(boid)
		print()