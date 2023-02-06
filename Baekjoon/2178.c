#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    int **arr;

    scanf("%d %d", &n, &m);
    arr = (int **)calloc((n + 2), sizeof(int *));
    for (int i = 0; i < n + 2; i++)
    {
        arr[i] = (int *)calloc((m + 2), sizeof(int));
    }
    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i = 0; i < n + 2; i++)
    {
        for (int j = 0; j < m + 2; j++)
        {
            printf("%d", arr[i][j]);
        }
        printf("\n");
    }
}