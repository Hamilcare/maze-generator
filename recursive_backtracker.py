from random import randrange #used to pick random neighbour cell

class maze(object):

	def __init__(self,height, width):
		self.height=height
		self.width=width

		self.grid = [[0 for row in range (0,height)] for col in range (0,width)]
		self.init_maze()


	def init_maze(self):
		for i in range (self.height):
			for j in range (self.width):
				self.grid[i][j] = cell(j,i)


	"""Create the maze by breaking walls and creating way"""
	def compute_maze(self):
		current_cell=self.grid[0][0]
		
		count_visited_cell = 0
		stack_of_visited_cell = []
		while count_visited_cell != self.height*self.width:
			current_cell.visited=True
			count_visited_cell+=1
			print(current_cell)
			print(count_visited_cell)
			unvisited_neighbours = self.get_unvisited_neighbours(current_cell)

			if(len(unvisited_neighbours)>0):
				chosen_cell = unvisited_neighbours[randrange(len(unvisited_neighbours))]
				stack_of_visited_cell.append(current_cell)
				current_cell.break_walls(chosen_cell)
				current_cell=chosen_cell

			elif len(stack_of_visited_cell)>0:
				current_cell=stack_of_visited_cell.pop()
	"""Use this to avoid confusion between indexes and coordinates"""
	def get_cell_from_coordinates(self,x,y):
		return self.grid[y][x]


	def get_unvisited_neighbours(self, cell):
		unvisited_neighbours=[]
		#We have to check if the cell is not on the maze's boundaries
		if(cell.x >0 and self.get_cell_from_coordinates(cell.x-1,cell.y).visited ==False):
			unvisited_neighbours.append(self.get_cell_from_coordinates(cell.x-1,cell.y))
		if(cell.x <self.width-1 and self.get_cell_from_coordinates(cell.x+1,cell.y).visited ==False):
			unvisited_neighbours.append(self.get_cell_from_coordinates(cell.x+1,cell.y))
		if(cell.y >0 and self.get_cell_from_coordinates(cell.x,cell.y-1).visited ==False):
			unvisited_neighbours.append(self.get_cell_from_coordinates(cell.x,cell.y-1))
		if(cell.y <self.height-1 and self.get_cell_from_coordinates(cell.x,cell.y+1).visited ==False):
			unvisited_neighbours.append(self.get_cell_from_coordinates(cell.x,cell.y+1))

		return unvisited_neighbours



"""Represent each cell of our maze
	defined by five booleans :
		-4 walls
		-visited or not
	and a position as two integers
"""
class cell(object):

	def __init__(self,x,y):
		self.nWall = True
		self.eWall = True
		self.sWall = True
		self.wWall = True

		self.visited = False
		self.x=x
		self.y=y

	def __str__(self):
		s="Coordinates: ("+str(self.x)+","+str(self.y)+")\n"
		s+="nWall: "+str(self.nWall)+"\n"
		s+="eWall: "+str(self.eWall)+"\n"
		s+="sWall: "+str(self.sWall)+"\n"
		s+="wWall: "+str(self.wWall)+"\n"

		return s

	
	#not perfect but satisfactory
	def __eq__(self, other):
		return self.x==other.x and self.y==other.y

	"""break_walls between to adjacent cells"""
	def break_walls(self,other):
		if self.x == other.x:
			if self.y > other.y: #self under other
				self.nWall=False
				other.sWall=False
			else: #self over other
				self.sWall=False
				other.nWall=False
		elif self.y == other.y:
			if self.x > other.x: #self at the right of other
				self.wWall=False
				other.eWall=False
			else:#self at the left of other
				self.eWall=False
				other.wWall=False


