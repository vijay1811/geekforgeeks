/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int mss(int arr[],int size,int n,int i,int memo[][size])
{
    if (n == 0)
    {
        return 0;
    }
    int idx ;
    idx = size - n;
    if (memo[i+1][n-1] == -100)
    {
        if ((i == -1) || (arr[idx]>arr[i]))
        {
            int a , b;
            a = arr[idx]+mss(arr,size,n-1,idx,memo);
            b = mss(arr,size,n-1,i,memo) ;
            memo[i+1][n-1] = (a >b)?a:b;
        }
        else
            memo[i+1][n-1] = mss(arr,size,n-1,i,memo);
    }
    return memo[i+1][n-1];
}

int main()
{
    int t;
    scanf("%d",&t);
    for (size_t i = 0; i < t; i++)
    {
        int n;
        scanf("%d",&n);
        int arr[n];
        for (size_t j = 0; j < n; j++)
        {
            scanf("%d",&arr[j]);
            /* code */
        }
        
        int memo[n+1][n];
          for (size_t k = 0; k < n+1; k++)
        {
            /* code */
            for (size_t l = 0; l < n; l++)
            {
                /* code */
                memo[k][l] = -100;
            }
            
        }
        printf("%d\n",mss(arr,n,n,-1,memo));
    }
    
    return 0; 
}
