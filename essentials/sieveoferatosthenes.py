from sys import stdin, stdout
def sieve(n):
	arr = [True for i in range(n+1)]
	p = 2
	while p*p <= n:
		if arr[p]:
			for i in range(2*p, n+1, p):
				arr[i] = False
		p += 1
	stdout.write(' '.join(str(p) for p in range(2, n+1) if arr[p]))

n = int(stdin.readline())
sieve(n)

# SIEVE OF ERATOSTHENES FINDS PRIME NUMBERS BELOW IN n IN O(sqrt(n)loglogn)
