#include <stdio.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i])
        i++;
    return i;
}

int main()
{
    int t;
    char buf[1001];

    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%s", buf);
        printf("%c%c\n", buf[0], buf[ft_strlen(buf) - 1]);
    }
}