#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

// 2차원 토마토 문제를 3차원으로!

int board[101][101][101];
int visited[101][101][101];

int dx[6] = {-1, 1, 0, 0, 0, 0};
int dy[6] = {0, 0, -1, 1, 0, 0};
int dz[6] = {0, 0, 0, 0, -1, 1};

int main()
{
    int m, n, h;
    cin >> m >> n >> h;
    queue<tuple<int, int, int>> Q;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                cin >> board[i][j][k];
                if (board[i][j][k] == 1)
                    Q.push(make_tuple(i, j, k));
                if (board[i][j][k] == 0)
                    visited[i][j][k] = -1;
            }
        }
    }
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 6; dir++)
        {
            int nz = get<0>(cur) + dz[dir];
            int nx = get<1>(cur) + dx[dir];
            int ny = get<2>(cur) + dy[dir];
            if (nz < 0 || nz >= h || nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (visited[nz][nx][ny] >= 0)
                continue;
            visited[nz][nx][ny] = visited[get<0>(cur)][get<1>(cur)][get<2>(cur)] + 1;
            Q.push(make_tuple(nz, nx, ny));
        }
    }
    int mx = 0;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                if (visited[i][j][k] == -1)
                {
                    cout << "-1\n";
                    return 0;
                }
                if (visited[i][j][k] > mx)
                    mx = visited[i][j][k];
            }
        }
    }
    cout << mx << '\n';
}