def edist(s1, s2):
	s1_len = len(s1)
	s2_len = len(s2)

	dp = [[None] * (s2_len+1) for i in range(s1_len+1)] 

	for i in range(s1_len + 1):
		for j in range(s2_len+1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(
						dp[i-1][j], # insert
						dp[i][j-1], # remove
						dp[i-1][j-1] # replace  
					)
	return dp

s1 = "abcdef"
s2 = "azced"

dp = edist(s1, s2)
for row in dp:
	print row

print dp[len(s1)][len(s2)]

# Time complexity O(len(s1) * len(s2))