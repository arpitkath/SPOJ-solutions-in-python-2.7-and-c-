/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
    static int[][] dp;
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int arr[]=new int[n];
		dp=new int[n][n];
		for(int i=0;i<n;i++){
		    for(int j=0;j<n;j++)
		    dp[i][j]=-1;
		}
		for(int i=0;i<n;i++)
		{
		    arr[i]=Integer.parseInt(br.readLine());
		}
		System.out.println(f(arr,0,arr.length-1));
	}
	public static int f(int arr[],int i,int j)
	{
	    if(i>j)
	    {
	        return 0;
	    }
	    if(dp[i][j]!=-1)
	    {
	        return dp[i][j];
	    }
	    int y=arr.length-(j-i+1)+1;
	    
	        dp[i][j]=Math.max(f(arr,i+1,j)+(y*arr[i]),f(arr,i,j-1)+(y*arr[j]));
	        return dp[i][j];
	    
	}
}
