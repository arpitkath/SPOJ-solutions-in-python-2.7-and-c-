# your code goes here
def rev(n):
    n=str(n)
    result=n[::-1]
    count=0
    for i in result:
        if i=="0":
            count+=1
        else:
            break
    return int(result[count:])
def revSum(s):
    s=s.split()
    a=s[0]
    b=s[1]
    return rev(rev(a)+rev(b))
n=int(raw_input())
for i in range(n):
    s=raw_input()
    print revSum(s)
 