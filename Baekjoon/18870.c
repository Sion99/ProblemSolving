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
    int *compressed;

    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    compressed = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        compressed[i] = arr[i];
    }
    qsort(arr, n, sizeof(int), compare);
}