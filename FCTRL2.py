# your code goes here
# your code goes here
def fact(n):
    r=n
    if n==1:
        return 1
    if n>1:
        return r*fact(n-1)
n=int(raw_input())
for i in range(n):
    n=int(raw_input())
    print fact(n)