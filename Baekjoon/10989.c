#include <stdio.h>

int main()
{
    int n;
    int arr[10001];
    int num;
    int count;

    for (int i = 0; i < 10001; i++)
    {
        arr[i] = 0;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        arr[num]++;
    }
    count = 0;
    while (count < n)
    {
        for (int i = 1; i < 10001; i++)
        {
            while (arr[i] > 0)
            {
                printf("%d\n", i);
                arr[i]--;
                count++;
            }
        }
    }
}