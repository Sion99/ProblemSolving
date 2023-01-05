#include <stdio.h>

int main()
{
    int chour;
    int cmin;
    int csec;
    scanf("%d:%d:%d", &chour, &cmin, &csec);

    int mhour;
    int mmin;
    int msec;
    scanf("%d:%d:%d", &mhour, &mmin, &msec);

    int realhour;
    int realmin;
    int realsec;

    if (mhour < chour)
    {
        mhour = mhour + 24;
    }

    if (msec < csec)
    {
        realsec = 60 + msec - csec;
        mmin = mmin - 1;
    }
    else
    {
        realsec = msec - csec;
    }

    if (mmin < cmin)
    {
        realmin = 60 + mmin - cmin;
        mhour = mhour - 1;
    }
    else
    {
        realmin = mmin - cmin;
    }
    realhour = mhour - chour;
    printf("%02d:%02d:%02d\n", realhour, realmin, realsec);
}