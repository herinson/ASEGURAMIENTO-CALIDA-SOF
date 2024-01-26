import time, random
from objs.constants import *
from objs.bubble_file import *
from objs.grid_file import *
from objs.shooter_file import *
from objs.game_objects import *
import pygame as pg
import pygame


pg.init()

pygame.init()
pygame.mixer.init()
#sonido
musicList =['sonido/coniferous-forest-142569.mp3', 'sonido/the-cradle-of-your-soul-15700.mp3', 'sonido/just-relax-11157.mp3']
pygame.mixer.music.load(musicList[0])
pygame.mixer.music.play()
track = 0

def main():
	

	#icono
	background = Background()
	icon = pg.image.load("images/globos.png")
	pg.display.set_icon(icon)


	
	gun = Shooter(pos = BOTTOM_CENTER)
	gun.putInBox()	

	grid_manager = GridManager()
	game = Game()	
	cheat_manager = CheatManager(grid_manager, gun)

	
	mouse_pos = (DISP_W/2, DISP_H/2)
	
	
	while not game.over:		

		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

			
			if event.type == pg.MOUSEMOTION: mouse_pos = pg.mouse.get_pos()
				
			
			if event.type == pg.MOUSEBUTTONDOWN: gun.fire()
			
			if event.type == pg.KEYDOWN:
				cheat_manager.view(event) 

				
				if event.key == pg.K_c and pg.key.get_mods() & pg.KMOD_CTRL:
					pg.quit()
					quit()

		
		background.draw()					

		grid_manager.view(gun, game)		

		gun.rotate(mouse_pos)					
		gun.draw_bullets()					

		game.drawScore()				

		pg.display.update()		
		clock.tick(60)					

	game.gameOverScreen(grid_manager, background)

	return

if __name__ == '__main__': 
	while True: main()