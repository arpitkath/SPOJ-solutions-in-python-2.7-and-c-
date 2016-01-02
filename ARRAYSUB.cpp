#include<iostream>
#include<cstdio>

int n,k;
long int arr[1000001];

long int max_k(int x)
{
	long int maxm=-1;
	for(int i=x;i<x+k;i++)
	{
		if(arr[i]>maxm)
			maxm=arr[i];
	}
	return maxm;
}

void print_ans()
{
	for(int i=0;i<n-k+1;i++)
	{
		printf("%ld ",max_k(i));
	}
}

int main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%ld",&arr[i]);
	}
	scanf("%d",&k);
	print_ans();
}