#include <stdio.h>
#include <stdlib.h>

int opening(int n)
{
    int n;

    n = 0;
    for (int i = 0; i < n; i++)
    {
        n++;
    }
    return n;
}

int main()
{
    int n, m;
    int t;
    int time;
    int cup;

    scanf("%d %d", &n, &m);
    time = 0;
    scanf("%d", &t);
    cup = opening(t);
    if (cup == 0)
    {
        printf("fail\n");
        return 0;
    }
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &t);
    }
}