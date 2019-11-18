#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long n; 
        scanf("%ld",&n);
        long a=(n-1)/3;
        long b=(n-1)/5;
        long d=(n-1)/15;
        long output = 3*a*(a+1)/2 + 5*b*(b+1)/2 - 15*d*(d+1)/2;
        printf("%ld\n",output);
    }
    return 0;
}

