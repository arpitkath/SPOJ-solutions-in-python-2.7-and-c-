#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    long long int t,i,j,p,x,h,n,k;
    scanf("%lld",&t);
    while(t--){        
              p=0;
              int a[1000000],count[10]={0};
              scanf("%lld",&n);
              for(i=0;i<n;i++){
                       scanf("%d ",&a[i]);
               }
               for(i=n-1;i>=0;i--){
                        count[a[i]]++;
                        for(j = a[i]+1; j < 10; j++){
                                if(count[j]>0){
                                 p=1;
                                 break;
                                }
                        }
                        if(p==1){
                                a[i] = j; count[j]--;
                                k=i+1;
                             for(j = 0;j < 10; j++){
                                        while(count[j]--)
                                        a[k++] = j;
                                }
                                break;
                        }
               }
             if(i >= 0) {
                        for(i = 0; i < n; i++)
                printf("%d", a[i]);
                        printf("\n");
                }else{
                 printf("-1\n");
                }
        }
        return 0;
    }
