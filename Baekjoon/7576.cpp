#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

int board[1001][1001];
int visited[1001][1001];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int n, m;

    cin >> m >> n;
    queue<pair<int, int>> Q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 1)
                Q.push({i, j});
            if (board[i][j] == 0)
                visited[i][j] = -1;
        }
    }
    while (!Q.empty())
    {
        pair<int, int> cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (visited[nx][ny] >= 0)
                continue;
            visited[nx][ny] = visited[cur.first][cur.second] + 1;
            Q.push({nx, ny});
        }
    }
    int mx = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (visited[i][j] == -1)
            {
                cout << -1 << '\n';
                return 0;
            }
            if (visited[i][j] > mx)
                mx = visited[i][j];
        }
    }
    cout << mx << '\n';
}