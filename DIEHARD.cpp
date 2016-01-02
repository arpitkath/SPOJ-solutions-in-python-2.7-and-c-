#include<cstdio>
#include<iostream>
using namespace std;

int arr[2600][2600];

int maxm(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}
int f(int a,int b,int c)
{
	if(a<=0 || b<=0)
		return 0;
	if(c==0)
	{
		if(arr[a][b]==-1)
		{
			arr[a][b]=f(a+3,b+2,1)+1;
		}
		return arr[a][b];
	}
	if(arr[a][b]==-1)
	{
		arr[a][b]=maxm(f(a-5,b-10,0),f(a-20,b+5,0))+1;
	}
	return arr[a][b];
}

int main()
{
	int t,a,b;
	scanf("%d",&t);
	while(t--)
	{
	    //cin>>a>>b;
	    for (int i = 0; i < 2600; i++)
            for (int j = 0; j <2600; j++)
                arr[i][j] = -1;
		scanf("%d %d",&a,&b);
		printf("%d\n",f(a,b,0)-1);
	}
}