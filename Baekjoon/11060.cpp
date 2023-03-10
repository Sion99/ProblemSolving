#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int board[1001];
int visited[1001];

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> board[i];
    }
    queue<pair<int, int>> Q;
    Q.push({0, 0});
    visited[0] = 1;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        if (cur.first == n - 1)
        {
            cout << cur.second << '\n';
            return 0;
        }
        for (int i = 1; i <= board[cur.first]; i++)
        {
            int next = cur.first + i;
            if (next >= n)
                continue;
            if (visited[next] == 1)
                continue;
            Q.push({next, cur.second + 1});
            visited[next] = 1;
        }
    }
    cout << "-1\n";
}