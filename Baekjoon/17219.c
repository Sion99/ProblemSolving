#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct hash hash;

struct hash
{
    char site[21];
    char pass[21];
};

int main()
{
    int n, m;
    hash *arr;
    char temp[21];

    scanf("%d %d", &n, &m);
    arr = (hash *)malloc(sizeof(hash) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s %s", arr[i].site, arr[i].pass);
    }
    for (int i = 0; i < m; i++)
    {
        scanf("%s", temp);
        for (int j = 0; j < n; j++)
        {
            if (strcmp(arr[j].site, temp) == 0)
            {
                printf("%s\n", arr[j].pass);
            }
        }
    }
}