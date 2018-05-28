import time
start = time.time()
n = input()
arr = [None] * (n+1)

def fib(n):
	global arr
	if n <= 1:
		arr[n] = n
		return arr[n]
	else:
		if arr[n] is None:
			arr[n] = fib(n-1) + fib(n-2)
			return arr[n]
		else:
			return arr[n]



fib(n)
print arr[1:]
print "Time taken: " + str(time.time() - start)
