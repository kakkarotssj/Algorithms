def findlcs(s1, s2, s1_index, s2_index):
	if s1_index == 0 or s2_index == 0:
		return 0
	elif s1[s1_index-1] == s2[s2_index-1]:
		return 1 + findlcs(s1, s2, s1_index-1, s2_index-1)
	else:
		return max(findlcs(s1, s2, s1_index, s2_index-1), findlcs(s1, s2, s1_index-1, s2_index))

print "Enter string 1"
s1 = raw_input()
print "Enter string 2"
s2 = raw_input()


ans = findlcs(s1, s2, len(s1), len(s2))
print ans


# TIME COMPLEXITY OF THIS APPROACH IS O(2^n)