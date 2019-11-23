#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
long primeFactors(long n) 
{ 
   long mp;
    while (n%2 == 0) 
    { 
        mp=2;
        n = n/2; 
    } 
    for (int i = 3; i <=n; i = i+2) 
    {
        while (n%i == 0) 
        { 
            n = n/i; 
            mp=i;
        } 
    } 
    return mp;
}
  
int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long n; 
        scanf("%ld",&n);
        long mp;
        mp=primeFactors(n);
        printf("%ld\n",mp);
    }
    return 0;
}

