#include <stdio.h>
#include <string.h>

int main(void)
{
    char input[100];
    char filtered[100];
    int length = 0;
    int i, j = 0;
    int check = 0;
    fgets(input, 100, stdin);

    for (i = 0; i < (int)strlen(input); i++)
    {
        if ((input[i] >= 'A' && input[i] <= 'Z') || (input[i] >= 'a' && input[i] <= 'z'))
        {
            filtered[j] = input[i];
            j++;
        }
    }

    filtered[j] = '\0';
    length = strlen(filtered);

    for (i = 0; i < length; i++)
    {
        if (filtered[i] >= 'A' && filtered[i] <= 'Z')
        {
            filtered[i] = filtered[i] - 'A' + 'a';
        }
    }

    for (i = 0; i < length / 2; i++)
    {
        if (filtered[i] == (filtered[length - 1 - i]))
        {
            check = 1;
        }
        else
        {
            check = 0;
            break;
        }
    }

    if (check)
    {
        printf("Yes\n");
    }

    else
    {
        printf("No\n");
    }

    return 0;
}