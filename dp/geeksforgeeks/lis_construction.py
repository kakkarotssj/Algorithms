from collections import defaultdict
import copy


dp = defaultdict(list)
numbers = map(int, raw_input().split())
count_numbers = len(numbers)
dp[0].append(numbers[0])
for i in range(1, count_numbers):
	for j in range(i):
		if numbers[j] < numbers[i]:
			if len(dp[j]) + 1 > len(dp[i]):
				dp[i] = copy.deepcopy(dp[j])
		if numbers[i] not in dp[i]:
			dp[i].append(numbers[i])

ans = dp[0]
for key, value in dp.items():
	if len(dp[key]) > len(ans):
		ans = dp[key]
for num in ans:
	print num,