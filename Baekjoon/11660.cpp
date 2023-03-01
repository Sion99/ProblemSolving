#include <iostream>
#include <vector>
// 나중에 다시 풀어보기!!
using namespace std;

int main()
{
    int n, m, temp;
    int startx, starty, endx, endy;

    cin >> n >> m;
    int arr[n * n];
    for (int i = 0; i < n * n; i++)
    {
        cin >> temp;
        if (i == 0)
            arr[i] = temp;
        else
        {
            arr[i] = arr[i - 1] + temp;
        }
    }
    for (int i = 0; i < n * n; i++)
    {
        cout << arr[i] << " ";
        if (i % n == n - 1)
            cout << endl;
    }
    for (int i = 0; i < m; i++)
    {
        cin >> starty >> startx >> endy >> endx;
        if (startx == endx && starty == endy)
            if (startx == 1 && starty == 1)
                cout << arr[0] << endl;
            else
                cout << arr[(endx - 1) * n + (endy - 1)] - arr[(endx - 1) * n + (endy - 2)] << endl;
        else
            cout << arr[(endx - 1) * n + (endy - 1)] - arr[(startx - 1) * n + (starty - 1)] << endl;
    }
}