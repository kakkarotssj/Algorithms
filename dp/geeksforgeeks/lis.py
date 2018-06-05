arr = map(int, raw_input().split())
len_arr = len(arr)
dp = [1] * (len_arr)

for i in range(1, len_arr):
	for j in range(i):
		if arr[j] < arr[i]:
			temp = dp[j] + 1
			if temp > dp[i]:
				dp[i] = temp

print max(dp)