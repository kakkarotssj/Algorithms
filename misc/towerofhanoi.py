'''
WHOLE LOGIC BEHIND THIS IS :

IF (N==1)	MOVE DISK FROM PEG A TO PEG B
ELSE
	MOVE N-1 DISKS FROM PEG C TO PEG B USING A AS AUXILARY SPACE
	MOVE DISK FROM PEG A TO PEG C
	MOVE N-1 DISKS FROM PEG B TO PEG C USING A AS AUXILARY SPACE


'''


n = input("Enter no of rings \n")

def towerofhanoi(n, frompeg, topeg, auxspace):
	if n == 1:
		print "Move disk %s from Peg %s to Peg %s" % (n, frompeg, topeg)
		return
	else:
		towerofhanoi(n-1, frompeg, auxspace, topeg)
		print "Move disk %s from peg %s to peg %s" % (n, frompeg, topeg)
		towerofhanoi(n-1, auxspace, topeg, frompeg)

towerofhanoi(n, 'A', 'C','B')