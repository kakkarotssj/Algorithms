from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
os = lambda i : stdout.write(str(i) + '\n')
olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')


def printchess(chess):
	for i in range(8):
		for j in range(8):
			print chess[i][j],
		print ""

def is_cell_valid(chess, nextx, nexty):
	if nextx >= 0 and nextx <= 7 and nexty >= 0 and nexty <= 7:
		if chess[nextx][nexty] == -1:
			return True
	return False

def utilknighttour(x, y, move_no, chess, movex, movey):
	if move_no == 64:
		return True
	else:
		for i in range(8):
			nextx = x + movex[i]
			nexty = y + movey[i]
			# print nextx, nexty

			if is_cell_valid(chess, nextx, nexty):
				chess[nextx][nexty] = move_no

				if utilknighttour(nextx, nexty, move_no+1, chess, movex, movey):
					return True
				else:
					chess[nextx][nexty] = -1

		return False


def knighttour():
	movex = [2, 1, -1, -2, -2, -1,  1, 2]
	movey = [1, 2,  2,  1, -1, -2, -2, -1]
	chess = [[-1 for _ in range(8)] for _ in range(8)]
	chess[0][0] = 0
	move_no = 1
	x, y = 0, 0

	if not utilknighttour(x, y, move_no, chess, movex, movey):
		os("Solution does not exist.")
	else:
		printchess(chess)

def main():
	knighttour()

if __name__ == '__main__':
	main()
