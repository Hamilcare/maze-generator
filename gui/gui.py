import sys
sys.path.append("../commonObjects")
from common import *

import pygame
from pygame.locals import *

cell_width=10
wall_width=int(cell_width/10)

def draw_maze(maze):
	pygame.init()

	frame = pygame.display.set_mode((cell_width*maze.width,cell_width*maze.height),RESIZABLE)
	#background = pygame.image.load("./gui/images/background.jpg").convert()
	#frame.blit(background,(0,0))
	frame.fill((255,255,255))
	pygame.display.update()
	#pygame.display.flip()
	#pygame.draw.line(frame,(0,0,0),(0,0),(55,55),2) 
	#pygame.display.flip()
	for i in range (maze.width):
		for j in range (maze.height):
			current_cell = maze.get_cell_from_coordinates(i,j)
			if current_cell.nWall:
				pygame.draw.line(frame,(0,0,0),(current_cell.x*(cell_width/2),current_cell.y*(cell_width/2)),(current_cell.x*(cell_width/2)+4,current_cell.y*(cell_width/2)),wall_width)
			if current_cell.sWall:
				pygame.draw.line(frame,(0,0,0),(current_cell.x*(cell_width/2),current_cell.y*(cell_width/2)+4),(current_cell.x*(cell_width/2)+4,current_cell.y*(cell_width/2)+4),wall_width)
			if current_cell.eWall:
				pygame.draw.line(frame,(0,0,0),(current_cell.x*(cell_width/2)+4,current_cell.y*(cell_width/2)),(current_cell.x*(cell_width/2)+4,current_cell.y*(cell_width/2)+4),wall_width)
			if current_cell.wWall:
				pygame.draw.line(frame,(0,0,0),(current_cell.x*(cell_width/2),current_cell.y*(cell_width/2)),(current_cell.x*(cell_width/2),current_cell.y*(cell_width/2)+4),wall_width)
			if current_cell.visited==False:
				pygame.draw.rect(frame,(255,0,0),(0,0,cell_width/2,cell_width/2))						
			#pygame.display.flip()
	pygame.draw.rect(frame,(0,255,0),(0,0,cell_width/2,cell_width/2))
	pygame.display.flip()

	int(input())