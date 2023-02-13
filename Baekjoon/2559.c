#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, k;
    int *arr;
    int sum;
    int max;

    max = -2147483648;
    scanf("%d %d", &n, &k);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    sum = 0;
    for (int i = 0; i < k; i++)
    {
        sum += arr[i];
    }
    if (sum > max)
        max = sum;
    for (int i = 0; i < n - k + 1; i++)
    {
        if (sum > max)
            max = sum;
        sum -= arr[i];
        sum += arr[i + k];
    }
    printf("%d\n", max);
}