s = raw_input()
n = len(s)

def recur_util(buff, s, i, j, n):
	if j == n:
		print ''.join(buff[:i])
		return
	
	# either put the character
	buff[i] = s[j]
	recur_util(buff, s, i+1, j+1, n)

	#first put the space and then character
	buff[i] = ' '
	buff[i+1] = s[j]
	recur_util(buff, s, i+2, j+1, n)

def recur(s, n):
	buff = [None]*(2*n-1)
	buff[0] = s[0]
	recur_util(buff, s, 1, 1, n)



recur(s, n)