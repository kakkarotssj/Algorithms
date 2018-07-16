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

def validate_row_col(ans, row, col):
	# validate row
	for i in range(4):
		if ans[row][i] == 1:
			return False
	
	# validate col
	for i in range(4):
		if ans[i][col] == 1:
			return False

	return True

def validate_diagonals(ans, row, col):
	# validate main diagonal
	i, j = row, col
	while i >=0 and j >=0:
		if ans[i][j] == 1:
			return False
		i -= 1
		j -= 1

	i, j = row, col
	while i <= 3 and j <= 3:
		if ans[i][j] == 1:
			return False
		i += 1
		j += 1

	# validate other diagonal
	i, j = row, col
	while i >= 0 and j <= 3:
		if ans[i][j] == 1:
			return False
		i -= 1
		j += 1

	i , j = row, col
	while i <= 3 and j >= 0:
		if ans[i][j] == 1:
			return False
		i += 1
		j -= 1

	return True



def isvalid(ans, row, col):
	row_col_status = validate_row_col(ans, row, col)
	diagonal_status = validate_diagonals(ans, row, col)

	if row_col_status and diagonal_status:
		return True
	else:
		return False

def util_n_queen(ans, queens_placed, col):
	if queens_placed == 4:
		return True
	
	for row in range(4):
		if isvalid(ans, row, col):
			ans[row][col] = 1
			queens_placed += 1
			col += 1
			if util_n_queen(ans, queens_placed, col):
				return True

			col -= 1
			ans[row][col] = 0
			queens_placed -= 1

	return False


def n_queen():
	ans = [[0 for _ in range(4)] for _ in range(4)]
	queens_placed = 0
	col = 0

	if util_n_queen(ans, queens_placed, col):
		print_grid(ans)
	else:
		os("No Solution exists.")


def main():
	n_queen()


main()