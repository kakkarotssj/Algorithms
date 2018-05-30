import time
start = time.time()

a, b = map(int, raw_input().split())
c = a
def naive_expo(a,b):
	for i in range(b-1):
		a *= c

naive_expo(a, b)
print "time taken: " + str(time.time() - start)
