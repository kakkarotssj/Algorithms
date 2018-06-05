print "Enter string 1"
s1 = raw_input()
print "Enter string 2"
s2 = raw_input()

def findlcs(s1, s2):
	lens1 = len(s1)
	lens2 = len(s2)

	dp = [[None] * (lens2+1) for i in range(lens1+1)]

	for i in range(lens1+1):
		for j in range(lens2+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp



dp = findlcs(s1, s2)
print dp[len(s1)][len(s2)]



# this dp approach to find length of lcs is O(lens1*lens2)