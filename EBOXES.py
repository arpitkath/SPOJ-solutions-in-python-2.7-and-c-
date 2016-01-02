# your code goes here
def f(s):
	s=s.split()
	s=map(int,s)
	n=s[0]
	k=s[1]
	f=s[3]
	return n+(k*(f-n)/(k-1))
t=int(raw_input())
for i in range(t):
	s=raw_input()
	print f(s)