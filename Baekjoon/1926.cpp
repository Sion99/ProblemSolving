#include <iostream>
#include <utility>
#include <queue>

using namespace std;

#define X first
#define Y second

int board[502][502];
bool visited[502][502];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int n, m;
    int maxn = 0;
    int count = 0;
    int sum;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] == 0 || visited[i][j])
                continue;
            count++;
            queue<pair<int, int>> Q;
            visited[i][j] = 1;
            Q.push({i, j});
            sum = 0;
            while (!Q.empty())
            {
                sum++;
                pair<int, int> cur = Q.front();
                Q.pop();
                for (int dir = 0; dir < 4; dir++)
                {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                        continue;
                    if (visited[nx][ny] || board[nx][ny] != 1)
                        continue;
                    visited[nx][ny] = 1;
                    Q.push({nx, ny});
                }
            }
            if (sum > maxn)
                maxn = sum;
        }
    }
    cout << count << '\n';
    cout << maxn << '\n';
}