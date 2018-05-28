
arr = map(int, raw_input().split())
arr_size = len(arr)
lis = [1] * arr_size

for i in range(1, arr_size):
	for j in range(i):
		if arr[i] > arr[j]:
			temp = lis[j] + 1
			if temp > lis[i]:
				lis[i] = temp

print max(lis)
