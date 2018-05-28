import time
start = time.time()


def fib(n, arr):
	if n < 2:
		arr[n] = n
		return n
	else:
		if arr[n] is None:
			arr[n] = fib(n-1, arr) + fib(n-2, arr)
			return arr[n]
		else:
			return arr[n]

n = input()
arr = [None] * (n+1)
number = fib(n, arr)
print number