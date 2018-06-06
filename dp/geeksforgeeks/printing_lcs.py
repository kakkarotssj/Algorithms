print "enter string 1"
str1 = raw_input()
print "Enter string 2"
str2 = raw_input()
rows = len(str1)
cols = len(str2)


def findlcs(str1, str2):
	dp = [[None] *(cols+1) for row in range(rows+1)]
	for row in range(rows+1):
		for col in range(cols+1):
			if row == 0 or col == 0:
				dp[row][col] = 0
			elif str1[row-1] == str2[col-1]:
				dp[row][col] = 1 + dp[row-1][col-1]
			else:
				dp[row][col] = max(dp[row-1][col], dp[row][col-1])

	return dp

dp = findlcs(str1, str2)
ans = []
i, j = rows, cols

while i >0 and j > 0:
	if str1[i-1] == str2[j-1]:
		ans.insert(0, str1[i-1])
		i -= 1
		j -=1
	else:
		if dp[i-1][j] > dp[i][j-1]:
			i -= 1
		else:
			j -= 1
print ''.join(ans)

# TIME COMPLEXITY WILL BE O(mn)
# starting from i = 0 and j = 0 wont work beacuse of equal numbers on i+1, j and i, j+1 might not lead to maximum number in the dp array