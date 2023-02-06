#include <stdio.h>
#include <stdlib.h>

int find_sum(int **arr, int a, int b, int x, int y)
{
    int sum;

    sum = 0;
    for (int i = a; i <= x; i++)
    {
        for (int j = b; j <= y; j++)
        {
            sum += arr[i][j];
        }
    }
    return sum;
}

int main()
{
    int n, m, k;
    int **arr;
    int sum;
    int a, b, x, y;

    scanf("%d %d", &n, &m);
    arr = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = (int *)malloc(sizeof(int) * m);
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    scanf("%d", &k);
    for (int i = 0; i < k; i++)
    {
        scanf("%d %d %d %d", &a, &b, &x, &y);
        sum = find_sum(arr, a - 1, b - 1, x - 1, y - 1);
        printf("%d\n", sum);
    }
}