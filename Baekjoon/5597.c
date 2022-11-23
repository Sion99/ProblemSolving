// B5 과제 안 내신 분..?
#include <stdio.h>
int main()
{
    int n;
    int arr[31];
    for (int i = 0; i < 31; i++)
    {
        arr[i] = 0;
    }
    for (int i = 0; i < 28; i++)
    {
        scanf("%d", &n);
        arr[n] = n;
    }
    for (int i = 1; i < 31; i++)
    {
        if (arr[i] == 0)
        {
            printf("%d\n", i);
        }
    }
}
