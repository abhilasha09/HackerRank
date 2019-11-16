#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
struct str
{
	char *str1,*str2,*temp;
	int n;
};
int main() 
{
int q;
scanf("%d",&q);
struct str a[q];
for(int i=0;i<q;i++)
{
a[i].str1 = (char *)malloc(sizeof(char)); 
a[i].str2= (char *)malloc(sizeof(char)); 
a[i].temp = (char *)malloc(sizeof(char));
}
for(int i=0;i<q;i++)
{
scanf("%s",a[i].str1);
scanf("%s",a[i].str2);
scanf("%d",&a[i].n);
}
for(int i=0;i<q;i++)
{
while(strlen(a[i].temp)<a[i].n)
{
    a[i].temp = a[i].str1; 
     a[i].str1= a[i].str2;
    strcat( a[i].temp, a[i].str2); 
     a[i].str2=  a[i].temp; 
    //printf("%s\n",temp);
}
printf("%c\n", a[i].temp[a[i].n-1]);
}
return 0;
}
