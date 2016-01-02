# your code goes here
def f(s):
	k=s[::-1]
	if s==k:
		return "YES"
	else:
		return "NO"
t=int(raw_input())
for i in range(t):
	s=raw_input()
	print f(s)