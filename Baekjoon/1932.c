#include <stdio.h>
#include <stdlib.h>

int find_max2(int **arr, int index, int n)
{
}

void find_max(int **arr, int index, int *max, int n, int *temp)
{
    int j;

    if (index == n)
    {
        if (*temp > *max)
        {
            *max = *temp;
        }
        *temp = 0;
    }
    else
    {
        j = 1;
        while()
    }
}

int main()
{
    int n;
    int **arr;
    int max;
    int temp;

    scanf("%d", &n);
    arr = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = (int *)malloc(sizeof(int) * (i + 1));
        for (int j = 0; j < i + 1; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    max = 0;
    temp = 0;
    find_max(arr, 0, &max, n, &temp);
    printf("%d\n", max);
}