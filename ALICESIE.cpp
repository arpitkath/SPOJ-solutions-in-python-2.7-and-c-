#include<iostream>
using namespace std;
int main()
{
 long int t,n,m;
 cin>>t;
 while(t--)
 {
  cin>>n;
  if(n%2==0)
  {
   m=n/2;
   cout<<m<<endl;
  }
  else
  {
   m=n/2+1;
   cout<<m<<endl;
  }
 }
 return 0;

}
