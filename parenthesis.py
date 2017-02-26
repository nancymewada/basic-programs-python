def matchparenthesis(text):
	stack = []
	parenthesis = {')':'(',']':'[','}':'{'}
	for i in text:
		if i in parenthesis.keys():
			if len(stack)>0:
				if stack.pop() != parenthesis[i]:
					return False
			else:
				return False
		elif i in parenthesis.values():
			stack.append(i)
	return  len(stack)<1


print matchparenthesis('{a{a} d} dddd')
print matchparenthesis('{{')
print matchparenthesis('{{}}')
print matchparenthesis('))')
print matchparenthesis('()(){}}')
print matchparenthesis('(][{}}')
