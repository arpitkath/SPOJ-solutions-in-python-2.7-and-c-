#include <stdio.h>
int maxm(int a,int b)
{
    if(a>=b)
    return a;
    else
    return b;
}
int main(void) {
	// your code goes here
	int s,n;
	scanf("%d %d",&s,&n);
	int mem[n+1][s+1];
	int size[n+1];
	int val[n+1];
	int i,j;
	for(i=1;i<=n;i++)
	{
	    scanf("%d %d",&val[i],&size[i]);
	}
	for(i=1;i<=n;i++)
	{
	    for(j=1;j<s+1;j++)
	    {
	        if(size[i]<=j)
	            mem[i][j]=maxm(mem[i-1][j],mem[i-1][j-size[i]]+val[i]);
	        else
	            mem[i][j]=mem[i-1][j];
	    }
	}
	printf("%d",mem[n][s]);
	return 0;
}

