def insertionsort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr
arr = [64, 34, 25, 12, 22, 11, 90]
arr = insertionsort(arr)
print arr

'''
WORST CASE : O(n*n)
BEST CASE : O(n) --->> IF ARRAY IS ALREADY SORTED
AUXILARY SPACE: O(1)
STABLE : YES
'''