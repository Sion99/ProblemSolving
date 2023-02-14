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
    int n, m;
    int *arr;
    int i, j, count;

    scanf("%d %d", &n, &m);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), compare);
    i = 0;
    j = n - 1;
    count = 0;
    while (i < j)
    {
        if (arr[i] + arr[j] == m)
        {
            count++;
            if (arr[i + 1] - arr[i] < arr[j] - arr[j - 1])
                i++;
            else
                j--;
        }
        else if (arr[i] + arr[j] < m)
            i++;
        else
            j--;
    }
    printf("%d\n", count);
    free(arr);
}