#include <stdio.h>
#include <stdlib.h>

int min(int a, int b, int c)
{
    if (a < b && a < c)
        return a;
    else if (b < a && b < c)
        return b;
    else
        return c;
}

int dp(int **arr, int n, int start)
{
    int sum;
    int last;

    sum = arr[0][start];
    last = start;
    for (int i = 1; i < n; i++)
    {
    }
}

void free_arr(int **arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        free(arr[i]);
    }
    free(arr);
}

int main()
{
    int n;
    int **arr;
    int flag;
    int sum;

    scanf("%d", &n);
    arr = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = (int *)malloc(sizeof(int) * 3);
        scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);
    }
    free_arr(arr, n);
}