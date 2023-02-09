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
    int *a;
    int *b;
    int index;
    int j, k;

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
    j = 0;
    k = 0;
    while (index < (n + m))
    {
        if (k == m)
        {
            printf("%d ", a[j]);
            j++;
        }
        else if (j == n)
        {
            printf("%d ", b[k]);
            k++;
        }
        else
        {
            if (a[j] < b[k])
            {
                printf("%d ", a[j]);
                j++;
            }
            else
            {
                printf("%d ", b[k]);
                k++;
            }
        }
        index++;
    }
    free(a);
    free(b);
}