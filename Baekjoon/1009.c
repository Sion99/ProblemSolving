#include <stdio.h>

int get_last_digit(int a, int b)
{
    int i;
    int num;

    i = 0;
    num = 1;
    while (i < b)
    {
        num *= a;
        num = num % 10;
        i++;
    }
    return num;
}

int main()
{
    int t;
    int a, b;
    int num;

    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &a, &b);
        if (a % 10 == 0)
        {
            num = 10;
        }
        else
        {
            num = get_last_digit(a, b);
        }
        printf("%d\n", num);
    }
}