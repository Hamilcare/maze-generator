import sys
sys.path.append("./algorithm")
from recursive_backtracker import *
sys.path.append("./gui")
from gui import *



def main():
	mymaze = maze(100,100)
	mymaze.compute_maze()
	draw_maze(mymaze)




if __name__ == "__main__":
    main()