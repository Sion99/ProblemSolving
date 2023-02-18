#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    if (*(int *)a > *(int *)b)
        return -1;
    else if (*(int *)a < *(int *)b)
        return 1;
    else
        return 0;
}

int main()
{
    int n, k;
    int *arr;

    scanf("%d %d", &n, &k);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), compare);
    printf("%d\n", arr[k - 1]);
    free(arr);
}