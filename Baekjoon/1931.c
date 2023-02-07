#include <stdio.h>
#include <stdlib.h>

typedef struct meeting meeting;

struct meeting
{
    int start;
    int end;
};

int static compare(const void *first, const void *second)
{
    if (((meeting *)first)->end > ((meeting *)second)->end)
        return 1;
    else if (((meeting *)first)->end < ((meeting *)second)->end)
        return -1;
    else
    {
        if (((meeting *)first)->start > ((meeting *)second)->start)
            return 1;
        else if (((meeting *)first)->start < ((meeting *)second)->start)
            return -1;
        return 0;
    }
}

int main()
{
    int n;
    int start, end;
    int count, k;
    meeting *arr;
    meeting last;

    scanf("%d", &n);
    arr = (meeting *)malloc(sizeof(meeting) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &start, &end);
        arr[i].start = start;
        arr[i].end = end;
    }
    qsort(arr, n, sizeof(meeting), compare);
    count = 0;
    last.start = 0;
    last.end = 0;
    k = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i].start < last.end)
            continue;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i].end > arr[j].end)
            {
                k = 1;
                last = arr[j];
                count++;
                break;
            }
        }
        if (k != 1)
        {
            last = arr[i];
            count++;
        }
        k = 0;
    }
    printf("%d\n", count);
    free(arr);
}