n = 7
range_n = n-1
d = (n*n) + 1

a= [[i for i in range(i,i+n)] for i in range(1,n*n,n)]
nd =n
c = 0
for i in range(0,(n/2)):
	for ab in range(i,nd-i):
		c += 1
		if c < d:
			print a[i][ab]
		else:
			break
	for cd in range(i+1,nd-i):
		c += 1
		if c < d:
			print a[cd][range_n-i]	
		else:
			break
	for ef in range(range_n-i-1,i-1-i,-1):
		c += 1
		if c < d:
			print a[range_n-i][ef]
		else:
			break
	for gh in range(range_n-i-1,i,-1):
		c += 1
		if c < d:
			print a[gh][i]
		else:
			break

