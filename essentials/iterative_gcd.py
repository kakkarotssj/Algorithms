def findgcd(x, y):
	minm = min(x,y)
	while minm > 0:
		if x%minm == 0 and y%minm ==0:
			return minm
		minm -= 1

x = input("Enter a number: ")
y = input("Enter a number: ")
ans= findgcd(x, y)
print ans
