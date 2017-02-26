def Stringreverse(st):
	if len(st)<2:
		return st
	return Stringreverse(st[1:]) +st[0]

print Stringreverse('nancy') #1 way not good as recursion uses more space


print 'nancy'[::-1] #2 way

st = 'nancy'
print ''.join([st[i] for i in range(len(st)-1,-1,-1)])#3 way
