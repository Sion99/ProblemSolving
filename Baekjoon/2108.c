#include <stdio.h>
#include <math.h>

int get_avg(int *neg, int *pos, int n)
{
    int sum;

    sum = 0;
    for (int i = 0; i < 4000; i++)
    {
        sum += (neg[i] * -i);
    }
    for (int i = 0; i < 4001; i++)
    {
        sum += (pos[i] * i);
    }
    if (sum < 0)
    {
        return (floor((sum / n) - 0.5));
    }
    else
    {
        return (sum / n + 0.5);
    }
}

int get_freq(int *neg, int *pos)
{
    int freq;
    int num;
    int freqcount;
    int memo;

    freq = 0;
    freqcount = 0;
    for (int i = 3999; i >= 0; i--)
    {
        if (neg[i] > freq)
        {
            freq = neg[i];
            num = -i;
            freqcount = 1;
        }
        else if (neg[i] == freq)
        {
            freqcount++;
            if (freqcount == 2)
                memo = -i;
        }
    }
    for (int i = 0; i < 4001; i++)
    {
        if (pos[i] > freq)
        {
            freq = pos[i];
            num = i;
            freqcount = 1;
        }
        else if (pos[i] == freq)
        {
            freqcount++;
            if (freqcount == 2)
                memo = i;
        }
    }
    if (freqcount == 1)
    {
        return (num);
    }
    else
    {
        return (memo);
    }
}

int main()
{
    int n;
    int neg[4000] = {
        0,
    };
    int pos[4001] = {
        0,
    };
    int num;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (num < 0)
        {
            neg[-num]++;
        }
        else
        {
            pos[num]++;
        }
    }
    printf("%d\n", get_avg(neg, pos, n));
    printf("%d\n", get_freq(neg, pos));
}