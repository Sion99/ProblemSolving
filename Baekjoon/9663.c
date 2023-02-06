#include <stdio.h>

int promising(int *arr, int index)
{
    int i;
    int diff;

    i = 1;
    while (i < index)
    {
        diff = arr[i] - arr[index];
        if ((i - index) == diff || (index - i) == diff || arr[i] == arr[index])
            return 0;
        else
            i++;
    }
    return 1;
}

void nqueen(int *arr, int index, int n, int *result)
{
    int j;

    if (promising(arr, index))
    {
        if (index == n)
        {
            *result += 1;
        }
        else
        {
            j = 1;
            while (j < n + 1)
            {
                arr[index + 1] = j;
                nqueen(arr, index + 1, n, result);
                j++;
            }
        }
    }
}

int main()
{
    int result;
    int i;
    int n;
    int arr[15];

    i = 0;
    result = 0;
    scanf("%d", &n);
    while (i < 11)
    {
        arr[i++] = 0;
    }
    nqueen(arr, 0, n, &result);
    printf("%d\n", result);
}