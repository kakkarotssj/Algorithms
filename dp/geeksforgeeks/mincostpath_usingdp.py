
def mincost(costs, m, n):
	dp = [[None for i in range(n)] for j in range(m)]
	dp[0][0] = costs[0][0]
	for col in range(1, n):
		dp[0][col] = dp[0][col-1] + costs[0][col]
	for row in range(1,m):
		dp[row][0] = dp[row-1][0] + costs[row][0]

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = costs[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

	return dp[m-1][n-1]



m = 3
n = 3
costs = [
		[1,2,3],
		[4,8,2],
		[1,5,3]
		]

ans = mincost(costs, m, n)
print ans

# TIME COMPLEXITY HERE WILL BE O(m*n)