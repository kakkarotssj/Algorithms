'''

(a+b)%c = (a%c + b%c)%c
(a*b)%c = ((a%c)*(b*%c))%c
(a-b)%c = ((a%c) - (b%c) + c)%c
(a/b)%c = ((a%c) * (b^(-1)%c))%c

'''

import time


a, b = map(int, raw_input().split())
start = time.time()

def better_expo(a, b):
	if b == 1:
		return a
	elif b % 2 == 0:
		return better_expo(a*a, b/2)
	else:
		return a*better_expo(a*a, (b-1)/2)

better_expo(a,b)
print "time taken: " + str(time.time() - start)