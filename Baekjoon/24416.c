#include <stdio.h>

int fib_recur(int n, int *result)
{
    if (n == 1 || n == 2)
    {
        (*result)++;
        return 1;
    }
    else
        return (fib_recur(n - 1, result) + fib_recur(n - 2, result));
}

void fib_dynamic(int *arr, int n, int *result)
{
    arr[1] = 1;
    arr[2] = 2;
    for (int i = 3; i <= n; i++)
    {
        arr[i] = arr[i - 1] + arr[i - 2];
        (*result)++;
    }
}

int main()
{
    int n;
    int a, b;
    int arr[41];

    scanf("%d", &n);
    a = 0;
    b = 0;
    fib_recur(n, &a);
    fib_dynamic(arr, n, &b);
    printf("%d %d\n", a, b);
}