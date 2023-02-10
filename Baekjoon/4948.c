#include <stdio.h>

int find_prime(int n)
{
    int i;

    i = 1;
    while (i * i < n)
    {
        if (n % i == 0)
        {
            return (0);
        }
        i++;
    }
    return (1);
}

int main()
{
    int n;
    int count;

    n = 1;
    while (1)
    {
        scanf("%d", &n);
        if (n == 0)
        {
            break;
        }
        count = 0;
        while (n <= 2 * n)
        {
            if (find_prime(n))
            {
                count++;
            }
            n++;
        }
        printf("%d\n", count);
    }
}