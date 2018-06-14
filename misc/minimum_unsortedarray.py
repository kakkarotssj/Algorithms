'''
FIND THE MINIMUM LENGTH OF UNSORTED SUBARRAY , SORTING WHICH WILL MAKE THE ARRAY SORTED

STEPS:
1). SCAN FROM LEFT TO RIGHT AND FIND INDEX S WHOSE ELEMENT IS GREATER THAN ITS NEXT ONE
2). SCAN FROM RIGHT TO LEFT AND FIND INDEX E WHOSE ELEMENT IS SMALLER THAN ITS NEXT TONE
3). FIND MINIMUM AND MAXIMUM IN THAT SUBARRAY
	A). Find the first element (if there is any) in arr[0..s-1] which is greater
	    than min, change s to index of this element
	B). Find the last element (if there is any) in arr[e+1..n-1] which is smaller
	    than max, change e to index of this element 
'''
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
arrlen = len(arr)
for i in range(arrlen-1):
	if arr[i] > arr[i+1]:
		s = i
		break
for i in range(arrlen-1, 0, -1):
	if arr[i] < arr[i-1]:
		e = i
		break
minm = min(arr[s:e+1])
maxm = max(arr[s:e+1])
for i in range(s):
	if arr[i] > minm:
		s = i
for i in range(arrlen-1, e, -1):
	if arr[i] < maxm:
		e = i
print "Indices are :", s, e
print "and array is :", arr[s: e+1]