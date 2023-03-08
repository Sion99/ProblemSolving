#include <iostream>
#include <queue>
#include <utility>
#include <string>

using namespace std;

int dx[8] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[8] = {0, 1, 0, -1, 1, -1, 1, -1};

int main()
{
    int w, h;
    while (1)
    {
        cin >> w >> h;
        if (w == 0 && h == 0)
            break;
        int board[51][51] = {
            0,
        };
        int visited[51][51] = {
            0,
        };
        int count = 0;
        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++)
                cin >> board[i][j];
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                if (board[i][j] == 0 || visited[i][j])
                    continue;
                count++;
                queue<pair<int, int>> Q;
                Q.push({i, j});
                visited[i][j] = 1;
                while (!Q.empty())
                {
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    for (int dir = 0; dir < 8; dir++)
                    {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if (nx < 0 || nx >= h || ny < 0 || ny >= w)
                            continue;
                        if (visited[nx][ny] || board[nx][ny] != 1)
                            continue;
                        Q.push({nx, ny});
                        visited[nx][ny] = 1;
                    }
                }
            }
        }
        cout << count << '\n';
    }
}
