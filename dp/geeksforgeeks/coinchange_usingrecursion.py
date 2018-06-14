
def count(coins, coinscount, reqsum):
	if reqsum == 0:
		return 1 # i.e include no coin hence one way to sum up the cum to the value reqsum

	elif reqsum < 0:
		return 0

	elif coinscount == 0 and reqsum > 0:
		return 0

	return count(coins, coinscount-1, reqsum) + count(coins, coinscount, reqsum-coins[coinscount-1])


reqsum = 10
coinscount = 4
coins = [2,5, 3, 6]
totalcombinations = count(coins, coinscount, reqsum)
print totalcombinations