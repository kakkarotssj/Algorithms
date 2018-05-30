import time
n = input()
start = time.time()

def check_prime(n):
	count = 0
	i = 1
	while i*i <= n:
		if n % i == 0:
			if i*i == n:
				count += 1
			else:
				count += 2
		i += 1
	if count == 2:
		return 1
	else:
		return -1

ans = check_prime(n)
if ans == 1:
	print str(n) + " is a prime number"
else:
	print str(n) + " is not a prime number"

print "Time taken: " + str(time.time() - start)