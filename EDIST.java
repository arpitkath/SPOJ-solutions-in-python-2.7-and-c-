/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        String a,b;
        while(t!=0)
        {
            t-=1;
            a=br.readLine();
            b=br.readLine();
            System.out.println(edit(a,b));
            
        }
	}
	static int [][] dp;
	public static int edit(String a,String b)
	{
	    int i,j;
	    dp=new  int[a.length()+1][b.length()+1];
	    for(i=0;i<=(a.length());i++)
	    {
	        dp[i][0]=i;
	    }
	    for(j=0;j<=(b.length());j++)
	    {
	        dp[0][j]=j;
	    }
	    for(i=1;i<=(a.length());i++)
	    {
	        for(j=1;j<=(b.length());j++)
	        {
	            if(a.charAt(i-1)==b.charAt(j-1))
	                dp[i][j]=dp[i-1][j-1];
	            else
	                dp[i][j]=Math.min(dp[i-1][j]+1,Math.min(dp[i-1][j-1]+1,dp[i][j-1]+1));
	        }
	    }
	    return dp[a.length()][b.length()];
	}
}
