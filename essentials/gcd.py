# IN PYTHON2 BUILT-IN LIBRARY IS IN FACTORIALS AND CAN BE IMPORTED AS 
# from factorials import gcd

def gcd(x,y):
	while y != 0:
		x, y = y, x%y
	return x

print "Enter numbers in fashion first one bigger and then smaller"
x, y = map(int, raw_input().split())
ans = gcd(x,y)
print ans
