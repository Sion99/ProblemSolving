#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>

using namespace std;
#define X first
#define Y second

int visited[101][101];
int board[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int n, m;
    cin >> n >> m;
    queue<pair<int, int>> Q;
    string s;
    fill(visited[0], visited[101], -1);
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        for (int j = 0; j < s.size(); j++)
        {
            board[i][j] = s[j] - 48;
        }
    }
    visited[0][0] = 0;
    Q.push({0, 0});
    while (!Q.empty())
    {
        pair<int, int> cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (visited[nx][ny] != -1 || board[nx][ny] != 1)
                continue;
            visited[nx][ny] = visited[cur.X][cur.Y] + 1;
            Q.push({nx, ny});
        }
    }
    cout << visited[n - 1][m - 1] + 1 << '\n';
}