from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
os = lambda i : stdout.write(str(i) + '\n')
olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')

def print_grid(grid):
	for i in range(9):
		for j in range(9):
			print grid[i][j],
		print ""

def get_freecell(grid):
	for row in range(9):
		for col in range(9):
 			if grid[row][col] == 0:
 				return [row, col]
 	return -1

def clash_in_row(grid, possibility, currentrow):
	for col in range(9):
		if grid[currentrow][col] == possibility:
			return True
	return False

def clash_in_col(grid, possibility, currentcol):
	for row in range(9):
		if grid[row][currentcol] == possibility:
			return True
	return False

def get_box_indices(current_index):
	if current_index in range(3):
		return 0,2
	elif current_index in range(3, 6):
		return 3, 5
	else:
		return 6, 8

def clash_in_box(grid, possibility, currentrow, currentcol):
	lowerrow, higherrow = get_box_indices(currentrow)
	lowercol, highercol = get_box_indices(currentcol)

	for i in range(lowerrow, higherrow):
		for j in range(lowercol, highercol):
			if grid[i][j] == possibility:
				return True
	return False


def solve(grid):
	current_cell = get_freecell(grid)
	if current_cell == -1:
		return True
	else:
		currentrow = current_cell[0]
		currentcol = current_cell[1]

		for possibility in range(1,10):
			# check if no clash in row
			if not clash_in_row(grid, possibility, currentrow):
				# check if no clash in col
				if not clash_in_col(grid, possibility, currentcol):
					# check if box satisfies condition
					if not clash_in_box(grid, possibility, currentrow, currentcol):
						grid[currentrow][currentcol] = possibility

						if solve(grid):
							return True

						grid[currentrow][currentcol] = 0

		return False


def main():
	grid = [[0 for _ in range(9)] for _ in range(9)]

	grid=[[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

	if solve(grid):
		print_grid(grid)
	else:
		os("Given sudoku can't be solved.")


if __name__ == '__main__':
	main()