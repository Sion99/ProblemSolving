#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 9; i++)
    {
        int temp;
        scanf("%d", &temp);
        n = n - temp;
    }
    printf("%d", n);
}