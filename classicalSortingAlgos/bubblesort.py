# def bubblesort(arr):
# 	for i in range(len(arr)):
# 		for j in range(len(arr) - i - 1):
# 			if arr[j] > arr[j+1]:
# 				arr[j], arr[j+1] = arr[j+1], arr[j]
# 	return arr
def improvedbubblesort(arr):
	for i in range(len(arr)):
		swapped = False
		for j in range(len(arr) - i -1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr
arr = [64, 34, 25, 12, 22, 11, 90]
arr = improvedbubblesort(arr)
print arr

'''
IMPROVEDBUBBLESORT IS SIMILAR TO BUBBLE SORT IT JUST BREAKS THE LOOP AND DONT CHECK
FURTHER IF THE ARRAY IS ALREADY SORTED.

WORST CASE : O(n*n)
BEST CASE  : O(n)
AUXILARY SPACE : O(1)
STABLE : YES

'''