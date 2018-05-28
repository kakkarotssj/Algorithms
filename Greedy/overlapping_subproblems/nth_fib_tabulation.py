def fib(n, arr):
	for i in range(2, n+1):
		if arr[i] is 0:
			arr[i] = arr[i-1] + arr[i-2]

	return arr[n]

n = input()
arr = [0] * (n+1)
arr[1] = 1

number = fib(n, arr)
print number
