def selectionsort(arr):
	for i in range(len(arr)):
		swapindex = i
		minm = arr[i]
		for j in range(i+1, len(arr)):
			if arr[j] < minm:
				swapindex = j
				minm = arr[j]
		arr[swapindex], arr[i] = arr[i], arr[swapindex]
	return arr
arr = [64, 34, 25, 12, 22, 11, 90]
arr = selectionsort(arr)
print arr

'''
WORST CASE : O(n*n)
AUXILARY SPACE : O(n)
STABLE : NO
GOOD POINT IS : IT ALWAYS DOES O(n) swaps
'''