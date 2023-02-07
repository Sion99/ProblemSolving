#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    char *str;
    int result;
    int temp;

    scanf("%d", &n);
    scanf("%d", &m);
    result = 0;
    str = (char *)malloc(sizeof(char) * m + 1);
    scanf("%s", str);
    str[m] = '\0';
    for (int i = 0; i < m; i++)
    {
        if (str[i + 1] == 'O' && str[i + 2] == 'I')
        {
            temp = 0;
            while (str[i] == 'I' && str[i + 1] == 'O')
            {
                i += 2;
                temp++;
                if (str[i] == 'I' && temp == n)
                {
                    temp--;
                    result++;
                }
            }
        }
    }
    printf("%d\n", result);
    free(str);
}