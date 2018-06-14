from collections import Counter
n = input()
for i in range(n):
	s = raw_input()
	if len(s) % 2 != 0:
		print -1
		continue
	s1 = s[:len(s)/2]
	s2 = s[len(s)/2:]
	counter1 = Counter(s1)
	counter2 = Counter(s2)
	ans = 0
	for key in counter1.keys():
		val1 = counter1[key]
		try:
			val2 = counter2[key]
			if val1 > val2:
				ans += val1 - val2
		except KeyError:
			ans += val1
	print ans
