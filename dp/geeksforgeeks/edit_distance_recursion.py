s1 = "saturday"
s2 = "sunday"

def edist(s1, s2, m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if s1[m-1] == s2[n-1]:
		return edist(s1, s2, m-1, n-1)
	return 1 + min(
					edist(s1, s2, m, n-1), 	# INSERTION
					edist(s1, s2, m-1, n),	# REMOVE
					edist(s1, s2, m-1, n-1)	# REPLACE
					)


ans = edist(s1, s2, len(s1), len(s2))
print ans

# TIME COMPLEXITY IS O(3^len(s1)