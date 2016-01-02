import java.util.*;
import java.lang.*;
import java.util.Scanner;
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner(System.in);
		int i=in.nextInt();
		while (i!=0)
		{
			System.out.println(sq(i));
			i=in.nextInt();
		}
	}
	public static int sq(int n)
	{
        int sum=(n*(n+1)*((2*n)+1))/6;
		return sum;
	}
}