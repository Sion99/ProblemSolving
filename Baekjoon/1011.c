#include <stdio.h>

int checkif(int start, int end)
{
    int term;

    term = 1;
    while (start < end)
    {
        start += term;
        term++;
    }
    if (start == end)
        return 1;
    else
        return 0;
}

int flyme(int x, int y)
{
    int result;
    int term;

    term = 1;
    result = 0;
    while (x < y - 1)
    {
        x += term;
        term++;
        result++;
    }
    if (x == y - 1)
        return (result + 1);
    else
    {
        term--;
        x -= term;
        result--;
    }
    return (result + 1);
}

int main()
{
    int t;
    int x, y;
    int result;

    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &x, &y);
        result = flyme(x, y);
        printf("%d\n", result);
    }
}