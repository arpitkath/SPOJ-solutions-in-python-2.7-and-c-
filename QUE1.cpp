#include<cstdio>
#include<algorithm>
#include<map>

using namespace std;

int n,inp[1001],pos[1001];
int ans[1001];

int f()
{
	int count=0,temp=0,j=0;
	map<int,int> arr;
	for(int i=0;i<n;i++)
	{
		arr[inp[i]]=pos[i];
	}
	sort(inp,inp+n);
	for(int i=0;i<n;i++)
	{
	    temp=arr[inp[i]];
	    //printf("%d",temp);
	    count=0;
	    j=0;
	    if(temp==0)
	    {
	        while(ans[j]!=-1)
	            j++;
	        ans[j]=inp[i];
	    }
		while(1 &&temp!=0)
		{
		    //if(j>n)
		    //break;
		    if(count==temp)
			{
			    while(ans[j]!=-1)
			        j++;
				ans[j]=inp[i];
				break;
			}
			if(ans[j]==-1)
		    {
				count++;
			}
			j+=1;

	    }
	}
	/*for(int i=0;i<n;i++)
	{
	    if(ans[i]==-1)
	    {
	        ans[i]=inp[n-1];
	        break;
	    }
	}*/
	for(int i=0;i<n-1;i++){
	    printf("%d ",ans[i]);
    }
    printf("%d\n",ans[n-1]);
}

int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&inp[i]);
			ans[i]=-1;}
		for(int i=0;i<n;i++)
			scanf("%d",&pos[i]);
		f();
		//for(int i=0;i<n;i++)
		//	printf("%d ",ans[i]);
	}
	return 0;
}