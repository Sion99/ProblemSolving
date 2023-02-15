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

int binarysearch(int *arr, int left, int right, int n)
{
    int count;

    count = 0;
    while (left <= right)
    {
        int mid = (left + right) / 2;

        if (arr[mid] > n)
        {
            count = right - mid;
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return count;
}
// 0 1 2 3 4 5 6 7 8 9
int main()
{
    int t;
    int n, m;
    int *a;
    int *b;
    int index, count;

    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &n, &m);
        a = (int *)malloc(sizeof(int) * n);
        b = (int *)malloc(sizeof(int) * m);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < m; i++)
        {
            scanf("%d", &b[i]);
        }
        qsort(a, n, sizeof(int), compare);
        qsort(b, m, sizeof(int), compare);
        index = 0;
        count = 0;
        for (int i = 0; i < n; i++)
        {
            while (index < m)
            {
                if (a[i] > b[index])
                {
                    index += 1;
                }
                else
                    break;
            }
            count += index;
        }
        printf("%d\n", count);
    }
}