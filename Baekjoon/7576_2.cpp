#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int board[1001][1001];
int visited[1001][1001];

int main()
{

    int n, m;
    cin >> m >> n;

    // 보관 후 하루가 지나면, 익은 토마토 인접한 익지 않은 토마토가 익음
    //  익은 토마토만 영향을 줌, 혼자 저절로 익는 경우 없음

    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    queue<pair<int, int> > Q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 1) {
                Q.push(make_pair(i, j));
            }
            if (board[i][j] == 0) {
                visited[i][j] = -1;
            }
        }
    }

    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
            {
                continue;
            }
            if (visited[nx][ny] != -1)
            {
                continue;
            }
            Q.push(make_pair(nx, ny));
            visited[nx][ny] = visited[cur.first][cur.second] + 1;
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