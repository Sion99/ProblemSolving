#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    int *arr;
    int temp;
    int start, end;
    int result;

    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    scanf("%d", &arr[0]);
    for (int i = 1; i < n; i++)
    {
        scanf("%d", &temp);
        arr[i] = arr[i - 1] + temp;
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &start, &end);
        if (start == 1)
        {
            result = arr[end - 1];
        }
        else
        {
            result = arr[end - 1] - arr[start - 2];
        }
        printf("%d\n", result);
    }
}