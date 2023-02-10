#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sort_string(char **str, int len)
{
    int i;
    int j;
    char *temp;

    i = 0;
    while (i < len - 1)
    {
        j = i + 1;
        while (j < len)
        {
            if (strcmp(str[i], str[j]) > 0)
            {
                temp = str[j];
                str[j] = str[i];
                str[i] = temp;
            }
            j++;
        }
        i++;
    }
}

int main()
{
    char str[1001];
    char **ends;
    int i;

    scanf("%s", str);
    i = 0;
    while (str[i])
        i++;
    ends = (char **)malloc(sizeof(char *) * i);
    i = 0;
    while (str[i])
    {
        ends[i] = &str[i];
        i++;
    }
    sort_string(ends, i);
    for (int j = 0; j < i; j++)
    {
        printf("%s\n", ends[j]);
    }
}