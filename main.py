import pygame as pg
import numpy as np
import time
import sys

from src.engine import Engine

if __name__ == "__main__":
	
	pg.init()

	height, width = 600, 1000
	numbers = 25

	eng = Engine(width, height)
	eng.initialization(numbers)
	
	pg.display.set_caption('Boids')
	screen = pg.display.set_mode((width, height))	

	bg = 25, 25, 25
	screen.fill(bg)

	loop = True
	while(loop):
		screen.fill(bg)

		ev = pg.event.get()
		for event in ev:
			if(event.type == pg.QUIT):
				loop = False

		eng.update()

		pg.draw.circle(screen, (255,0,0), eng.target.astype(int), 4)

		for boid in eng.boids:			
			init = boid.position.astype(int)
			end = init + 7*(boid.velocity / np.linalg.norm(boid.velocity))
			#end = init + boid.velocity

			pg.draw.circle(screen, (0,255,0), init.astype(int), 2)
			pg.draw.line(screen, (0, 0, 255), init.astype(int), end.astype(int))

		pg.display.flip()
		time.sleep(0.05)
	
	pg.quit()