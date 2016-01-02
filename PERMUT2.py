n = input()
while n!=0:
    a = map(int,raw_input().split())
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    if a==b:print "ambiguous"
    else:print "not ambiguous"
    n=input()
  