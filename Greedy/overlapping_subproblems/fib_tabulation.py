import time
start = time.time()

n = input()
arr = [0] * (n+1)
arr[1] = 1

def fib(n, arr):
	for i in range(2, n+1):
		arr[i] = arr[i-1] + arr[i-2]

	return arr


arr = fib(n, arr)
print arr[1:]
print "Time taken: " + str(time.time() - start)