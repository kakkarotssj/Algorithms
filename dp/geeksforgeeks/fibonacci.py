print "Enter the number of fibonacci sequences you wish to print"
n = input()



dp = [0] * (n+1)
def fib(n):
	global dp

	if n < 3:
		dp[n] = 1
		return dp[n]
	else:
		if dp[n] == 0:
			dp[n] = fib(n-1) + fib(n-2)
		return dp[n]
		

fib(n)
for num in dp[1:]:
	print num,
