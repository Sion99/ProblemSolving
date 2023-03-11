#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int t, h, w;
    cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
        cin >> h >> w;
        char board[101][101] = {
            0,
        };
        bool visited[101][101] = {
            0,
        };
        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++)
                cin >> board[i][j];
        int count = 0;
        int sum;
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                if (board[i][j] == '#' && visited[i][j] == 0)
                {
                    queue<pair<int, int>> Q;
                    Q.push({i, j});
                    visited[i][j] = 1;
                    sum = 0;
                    while (!Q.empty())
                    {
                        auto cur = Q.front();
                        Q.pop();
                        sum++;
                        for (int dir = 0; dir < 4; dir++)
                        {
                            int nx = cur.first + dx[dir];
                            int ny = cur.second + dy[dir];
                            if (nx < 0 || nx >= h || ny < 0 || ny >= w)
                                continue;
                            if (board[nx][ny] == '.' || visited[nx][ny])
                                continue;
                            Q.push({nx, ny});
                            visited[nx][ny] = 1;
                        }
                    }
                    if (sum >= 1)
                        count++;
                }
            }
        }
        cout << count << '\n';
    }
}