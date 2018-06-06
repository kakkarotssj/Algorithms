# AABEBCDD --> ABD
# CONDITION IN THIS QUESTION IS TWO SUBSEQUENCES WON'T HAVE SAME STRING CHARACTER AT SAME POSITION
# THIS QUESTION IS JUST SIMPLY THE LCS BUT IF TWO CHARACTERS ARE SAME THEIR INDICES HAVE TO BE DIFFERENT


def lrs(s):
	ssize = len(s)
	dp = [[None] * (ssize+1) for i in range(ssize+1)]

	for i in range(ssize+1):
		for j in range(ssize+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif s[i-1] == s[j-1] and i != j:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp


s = raw_input()
dp = lrs(s)
ssize = len(s)
i = ssize
j = ssize

ans = []
while i > 0 and j > 0:
	if dp[i][j] == dp[i-1][j-1] + 1:
		ans.insert(0, s[i-1])
		i -=1 
		j -=1
	else:
		if dp[i-1][j] == dp[i][j]:
			i -= 1
		else:
			j -= 1

print ''.join(ans)