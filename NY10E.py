l=[[0 for i in range(10)] for j in range(66)]
for i in range(10):
    l[0][i]=1
for i in range(1,66):
    for j in range(10):
        for k in range(j+1):
            l[i][j]+=l[i-1][k]
t=int(raw_input())
for i in range(1,t+1):
    a,b=map(int,raw_input().split())
    print "%d %d"%(i,l[b][9])