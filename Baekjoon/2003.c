#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    int *arr;
    int sum;
    int count;

    scanf("%d %d", &n, &m);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    count = 0;
    for (int i = 0; i < n; i++)
    {
        sum = 0;
        for (int j = i; j < n; j++)
        {
            sum += arr[j];
            if (sum == m)
            {
                count++;
            }
        }
    }
    printf("%d\n", count);
}