#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    if (*(int *)a < *(int *)b)
        return -1;
    else if (*(int *)a > *(int *)b)
        return 1;
    else
        return 0;
}

int main()
{
    int n;
    int *arr;
    int count;
    int max;

    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    count = 1;
    max = 0;
    qsort(arr, n, sizeof(int), compare);
    for (int i = 1; i < n; i++)
    {
        if (count == 5)
        {
            break;
        }
        if (arr[i] - arr[i - 1] == 1)
        {
            count++;
        }
        else
        {
            if (count > max)
                max = count;
            count = 1;
        }
    }
    if (max > count)
    {
        printf("%d\n", 5 - max);
    }
    else
    {
        printf("%d\n", 5 - count);
    }
}