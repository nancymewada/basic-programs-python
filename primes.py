def primenums(n):
	primes = []
	if n<2:
		primes=[]
	elif n == 2:
		primes=[2]
	else:
		primes = [2]
		for num in range(3,n+1,2):
			k=2
			while k <= num**0.5:
				if num%k == 0 :
					break
				k+=1
			else:
				primes.append(num)
	return primes


n = int(input('Enter range: '))

print primenums(n)