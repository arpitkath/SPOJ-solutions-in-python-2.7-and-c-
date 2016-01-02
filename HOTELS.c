#include <stdio.h>

int main(void) {
	// your code goes here
	int n,m;
	scanf("%d %d",&n,&m);
	int arr[n];
	int i,l=0,sum=0,maxm=0;
	for(i=0;i<n;i++)
	{
	    scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
	    sum+=arr[i];
	    while(sum>m)
	    {
	        sum-=arr[l];
	        l+=1;
	    }
	    if(sum>maxm)
	    maxm=sum;
	}
	printf("%d",maxm);
	return 0;
}

