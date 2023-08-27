#include <stdio.h>

int n;

int main(){
    //scan how many rows we need
    printf("how many rows do you need (max:50)\n");
    scanf(" %d",&n);
    //if it is more than 10 dont make the pyramid
    if (n<=20)
    //make an array with len of enough
    {int arr[20][40];
    //make the top of the pyramid 1
    arr[0][n]=1;
    //print first row if the number is 0 print space 
    for(int i=0;i<2*n;i++)if(arr[0][i]==0)printf(" ");else printf("%d",arr[0][i]);
    //calc other rows as sum of [col-1][row-1]+[col-1][row+1] and print the result
    for(int i=1;i<n;i++){printf("\n");for(int j=0;j<2*n;j++){
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j+1];
        if(arr[i][j]==0)printf(" ");else printf("%d",arr[i][j]);
    };};}}