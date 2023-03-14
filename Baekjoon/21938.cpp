#include <iostream>
#include <queue>
#include <utility>

using namespace std;

typedef struct pixel
{
    int r;
    int g;
    int b;
} pixel;

pixel board[1002][1002];
bool real[1002][1002];
bool visited[1002][1002];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int main()
{
    int n, m, t;
    int count = 0;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> board[i][j].r >> board[i][j].g >> board[i][j].b;
        }
    }
    cin >> t;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (board[i][j].r + board[i][j].g + board[i][j].b >= 3 * t)
                real[i][j] = 1;
        }
    }
    queue<pair<int, int>> Q;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (real[i][j] == 1 && visited[i][j] == 0)
            {
                Q.push({i, j});
                visited[i][j] = 1;
                while (!Q.empty())
                {
                    auto cur = Q.front();
                    Q.pop();
                    for (int dir = 0; dir < 4; dir++)
                    {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if (nx < 1 || nx > n || ny < 1 || ny > m)
                            continue;
                        if (real[i][j] == 0 || visited[i][j] == 1)
                            continue;
                        Q.push({i, j});
                        visited[i][j] = 1;
                    }
                }
                count++;
            }
        }
    }
    cout << count << '\n';
}