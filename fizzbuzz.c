#include <stdio.h>
void fizzbuzz(int a){
int x=1; //if x is still 1 by the end of the func print the number
  if (!(a%3)){//cheks if a divided by 3 has no remider !0=1=true. 3 comes first because fizz comes first too
    printf("Fizz");
    x=0;};
  if(!(a%5)){//cheks if a divided by 5 has no remider !0=1=true
    printf("Buzz");
    x=0;};
    if(x)//cheks the value of x
    printf("%i",a);
    return 0;//func compiled successfully
}


int main()
{
    for (int i=0;i<=100;i++){//run func for numberz 1 to 100
        fizzbuzz(i);
        printf("\n");
    }

    return 0;
}
