# LOGIC BEHIND CALCULATING LCM IS JUST MULTIPLYING BOTH THE NUMBERS AND DIVIDE
# IT BY THEIR GCD

from fractions import gcd
def lcm(x,y):
	return (x*y) / gcd(x,y)

print "Enter two numbers. Bigger one first"
x, y = map(int, raw_input().split())
ans = lcm(x,y)
print ans
