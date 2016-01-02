# your code goes here
def f(s):
	s=s.split()
	s=map(int,s)
	a=s[0]
	b=s[1]
	return (a**2)-(2*b)
t=int(raw_input())
for i in range(t):
	s=raw_input()
	print f(s)