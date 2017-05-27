import sys
sys.path.append("./commonObjects")
from common import *

sys.path.append("./algorithm")
import recursive_backtracker 

sys.path.append("./gui")
from gui import *

import time


def main():
	print("coucou")
	mymaze = maze(100,100)
	start = time.time()
	recursive_backtracker.compute_maze(mymaze)
	end = time.time()
	print("maze generated in "+str(end-start)+"second")
	draw_maze(mymaze)
	
	



if __name__ == "__main__":
    main()

def test_all_cells_visited_using_backtracker():
	mymaze = maze(100,100)
	recursive_backtracker.compute_maze(mymaze)
	for i in range(mymaze.width):
		for j in range(mymaze.height):
			assert mymaze.get_cell_from_coordinates(i,j).visited==True
