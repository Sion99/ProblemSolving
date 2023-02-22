#include <stdio.h>

int main()
{
    char str[101];

    scanf("%s", str);
    int i;

    i = 0;
    while (str[i])
    {
        if (str[i] >= 'a' && str[i] <= 'z')
            str[i] -= 32;
        else if (str[i] >= 'A' && str[i] <= 'Z')
            str[i] += 32;
        printf("%c", str[i]);
        i++;
    }
    printf("\n");
}