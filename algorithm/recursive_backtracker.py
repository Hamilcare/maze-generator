from random import randrange #used to pick random neighbour cell


"""Create the maze by breaking walls and creating way"""
def compute_maze(self):
	current_cell=self.grid[0][0]
	
	count_visited_cell = 0
	stack_of_visited_cell = []
	while count_visited_cell != self.height*self.width:
		if current_cell.visited == False:
        		current_cell.visited=True
        		count_visited_cell+=1
#		print(current_cell)
#		print(count_visited_cell)
		unvisited_neighbours = self.get_unvisited_neighbours(current_cell)

		if(len(unvisited_neighbours)>0):
			chosen_cell = unvisited_neighbours[randrange(len(unvisited_neighbours))]
			stack_of_visited_cell.append(current_cell)
			current_cell.break_walls(chosen_cell)
			current_cell=chosen_cell

		elif len(stack_of_visited_cell)>0:
			current_cell=stack_of_visited_cell.pop()

