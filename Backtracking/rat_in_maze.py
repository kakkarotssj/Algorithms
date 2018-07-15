from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
os = lambda i : stdout.write(str(i) + '\n')
olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')


def print_grid(grid):
	for i in range(4):
		for j in range(4):
			print grid[i][j],
		print ""

def cell_valid(x, y, maze):
	if x <= 3 and x >= 0 and y <= 3 and y >= 0:
		if maze[x][y] == 1:
			return True
	return False

def util_solve_maze(maze, ans, x, y):
	if x == 3 and y == 3:
		ans[x][y] = 1
		return True

	if cell_valid(x+1, y, maze):
		ans[x+1][y] = 1
		if util_solve_maze(maze, ans, x+1, y):
			return True
		ans[x+1][y] = 0

	if cell_valid(x, y+1, maze):
		ans[x][y+1] = 1
		if util_solve_maze(maze, ans, x, y+1):
			return True
		ans[x][y+1] = 0

	return False


def solve_maze():
	maze = [[1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1]]

	os("Maze given :")
	print_grid(maze)
	print "\n"

	ans = [[0 for _ in range(4)] for _ in range(4)]
	ans[0][0] = 1

	if util_solve_maze(maze, ans, 0, 0):
		print_grid(ans)
	else:
		os("Solution does not exist.")


def main():
	solve_maze()
	

main()