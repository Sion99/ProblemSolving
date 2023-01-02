#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int a0 = 0;
    int a1 = 1;
    int a2 = 0;
    if (n < 2)
    {
        printf("%d\n", n);
    }
    else
    {
        for (int i = 1; i < n; i++)
        {
            a2 = a1 + a0;
            a0 = a1;
            a1 = a2;
        }
        printf("%d\n", a2);
    }
}