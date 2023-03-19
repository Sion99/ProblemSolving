#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int board[101][101];
bool visited[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int m, n, k;
    int sx, sy, ex, ey;
    cin >> m >> n >> k;

    for (int i = 0; i < k; i++)
    {
        cin >> sx >> sy >> ex >> ey;
        for (int j = sy; j < ey; j++)
        {
            for (int k = sx; k < ex; k++)
            {
                board[k][j] = 1;
            }
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (board[i][j] == 0)
                visited[i][j] = 1;
        }
    }
    queue<pair<int, int>> Q;
    vector<int> v;
    int count = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (board[i][j] == 1 && visited[i][j] == 0)
            {
                Q.push({i, j});
                visited[i][j] = 1;
                count = 0;
                while (!Q.empty())
                {
                    auto cur = Q.front();
                    Q.pop();
                    count++;
                    for (int dir = 0; dir < 4; dir++)
                    {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                            continue;
                        if (board[nx][ny] == 0 || visited[nx][ny] == 1)
                            continue;
                        Q.push({nx, ny});
                        visited[nx][ny] = 1;
                    }
                }
                v.push_back(count);
            }
        }
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << ' ';
    cout << '\n';
}