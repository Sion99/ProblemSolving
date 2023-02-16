#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_strlen(char *str)
{
    int count;

    count = 0;
    while (str[count])
        count++;
    return count;
}

int main()
{
    int n;
    char **files;
    char buf[52];
    int result;
    char answer[52];

    scanf("%d", &n);
    files = (char **)malloc(sizeof(char *) * (n + 1));
    for (int i = 0; i < n; i++)
    {
        scanf("%s", buf);
        files[i] = (char *)malloc(sizeof(char) * ft_strlen(buf));
        strcpy(files[i], buf);
        files[i][ft_strlen(buf)] = 0;
    }
    files[n] = 0;
    for (int i = 0; i < ft_strlen(files[0]); i++)
    {
        result = 0;
        for (int j = 0; j < n - 1; j++)
        {
            if (files[j][i] != files[j + 1][i])
            {
                result = 1;
                break;
            }
        }
        if (result == 0)
        {
            answer[i] = files[0][i];
        }
        else
        {
            answer[i] = '?';
        }
    }
    answer[ft_strlen(files[0])] = 0;
    printf("%s\n", answer);
}