import pygame as pg
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

		for boid in eng.boids:
			pg.draw.circle(screen, (0,255,0), boid.position.astype(int), 2)

		pg.display.flip()
		time.sleep(0.05)
	
	pg.quit()