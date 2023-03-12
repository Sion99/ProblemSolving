#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int board[51][51];
bool visited[51][51];

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

int main()
{
    int n, m;
    cin >> n >> m;
    queue<pair<int, int>> Q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 1)
            {
                visited[i][j] = 1;
                Q.push({i, j});
                board[i][j] = 0;
            }
        }
    }
    int mx = 0;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 8; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (visited[nx][ny])
                continue;
            Q.push({nx, ny});
            visited[nx][ny] = 1;
            board[nx][ny] = board[cur.first][cur.second] + 1;
            if (mx < board[nx][ny])
                mx = board[nx][ny];
        }
    }
    cout << mx << '\n';
}