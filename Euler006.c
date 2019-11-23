#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

long long sqsum(long long n)
{
    return (n*(n+1)*(2*n+1))/6;
    
}
long long sumsq(long long n)
{
    long long sum=(n*(n+1))/2;
    return sum*sum;
}


int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long long n; 
        scanf("%lld",&n);
        long long sum=sumsq(n)-sqsum(n);
        printf("%lld\n",sum);
    }
    return 0;
}

