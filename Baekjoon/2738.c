#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    int arr[100][100];
    int temp;

    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &temp);
            arr[i][j] += temp;
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}