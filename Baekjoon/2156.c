#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int *wine;
    //    int max;
    int sum;
    int check;

    scanf("%d", &n);
    wine = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &wine[i]);
    }
    sum = 0;
    check = 0;
    for (int i = 0; i < n; i++)
    {
        sum += wine[i];
        if (check == 1)
        {
            i++;
            check = 0;
        }
        else
            check++;
    }
    printf("%d\n", sum);
}