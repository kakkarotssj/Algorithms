import time
n = input()
start = time.time()
def check_prime(n):
	for i in range(2,n):
		if n % i == 0:
			return -1
			break
	return 1

ans = check_prime(n)
if ans == 1:
	print str(n) + " is a prime number"
else:
	print str(n) + " is a not a prime number"

print "Time taken: " + str(time.time() - start)

# THIS SOLVES PROBLEM IN O(N)