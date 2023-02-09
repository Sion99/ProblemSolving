#include <stdio.h>

int find_max(int *arr)
{
    int max;

    max = 0;
    for (int i = 0; i < 9; i++)
    {
        if (i == 6)
        {
            if ((arr[i] + 1) / 2 > max)
            {
                max = (arr[i] + 1) / 2;
            }
        }
        else
        {

            if (arr[i] > max)
            {
                max = arr[i];
            }
        }
    }
    return (max);
}

int main()
{
    char str[7];
    int i;
    int flag[9];
    int num;

    scanf("%s", str);
    for (int j = 0; j < 9; j++)
    {
        flag[j] = 0;
    }
    i = 0;
    while (str[i])
    {
        num = str[i] - '0';
        if (num == 9)
            flag[6]++;
        else
            flag[num]++;
        i++;
    }
    printf("%d\n", find_max(flag));
}