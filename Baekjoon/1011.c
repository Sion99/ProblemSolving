#include <stdio.h>

int main()
{
    //    int t;
    //    int x, y;
    //    int result;
    int arr[50000];
    int temp, k;

    temp = 0;
    k = 1;
    for (int i = 0; i < 50000; i++)
    {
        arr[i] = temp;
        temp += k;
        k++;
    }
    for (int i = 0; i < 50000; i++)
    {
        printf("%d ", arr[i]);
    }

    // scanf("%d", &t);
    // for (int i = 0; i < t; i++)
    // {
    //     scanf("%d %d", &x, &y);
    //     result = flyme(y - x);
    //     printf("%d\n", result);
    // }
}