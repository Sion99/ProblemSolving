#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    if (*(int *)a > *(int *)b)
        return 1;
    else if (*(int *)a < *(int *)b)
        return -1;
    else
        return 0;
}

int main()
{
    int n;
    int *arr;
    int x;
    int count;
    int i, j;

    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    scanf("%d", &x);
    count = 0;
    qsort(arr, n, sizeof(int), compare);
    i = 0;
    j = n - 1;
    while (i < j)
    {
        if (arr[i] + arr[j] == x)
        {
            count++;
            if (arr[i + 1] - arr[i] < arr[j] - arr[j - 1])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        else if (arr[i] + arr[j] > x)
        {
            j--;
        }
        else if (arr[i] + arr[j] < x)
        {
            i++;
        }
    }
    free(arr);
    printf("%d\n", count);
}