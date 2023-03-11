#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int board[100001];
bool visited[100001];

int main()
{
    int n, start;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> board[i];
    }
    cin >> start;
    queue<pair<int, int>> Q;
    Q.push({start - 1, 1});
    visited[start - 1] = 1;
    int count = 0;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        count++;
        int arr[2] = {cur.first + board[cur.first], cur.first - board[cur.first]};
        for (int i = 0; i < 2; i++)
        {
            if (arr[i] < 0 || arr[i] >= n)
                continue;
            if (visited[arr[i]] == 1)
                continue;
            Q.push({arr[i], cur.second + 1});
            visited[arr[i]] = 1;
        }
    }
    cout << count << '\n';
}