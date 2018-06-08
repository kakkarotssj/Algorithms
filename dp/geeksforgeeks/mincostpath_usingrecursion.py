import sys
def mincost(costs, m, n):
	if m < 0 or n <0:
		return sys.maxsize
	elif m ==0 and n ==0:
		return costs[0][0]
	else:
		return costs[m][n] + min(mincost(costs, m-1, n), mincost(costs, m, n-1), mincost(costs, m-1, n-1))




m = 3
n = 3
costs = [
		[1,2,3],
		[4,8,2],
		[1,5,3]
		]

ans = mincost(costs, m-1, n-1)
print ans

# TIME COMPLEXITY IS O(3^m)