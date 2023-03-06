#include <iostream>
#include <queue>

using namespace std;

int board[1000001];

int main()
{
    int a, k;
    queue<int> Q;
    cin >> a >> k;
    Q.push(a);
    board[a] = 0;
    while (!Q.empty())
    {
        int cur = Q.front();
        Q.pop();
        if (cur == k)
        {
            cout << board[cur] << '\n';
            break;
        }
        int arr[2] = {cur + 1, cur * 2};
        for (int i = 0; i < 2; i++)
        {
            if (arr[i] > k)
                continue;
            if (board[arr[i]] > 0)
                continue;
            Q.push(arr[i]);
            board[arr[i]] = board[cur] + 1;
        }
    }
}