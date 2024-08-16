#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

void solution()
{

    int r, c;
    cin >> c >> r;

    // 지훈이 위치, 불 위치
    // 지훈이는 미로 가장자리로 가야 탈출
    // 동시에 불도 옆으로 퍼짐

    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    char board[1001][1001] = {0, };
    int jihoon_visited[1001][1001] = {0, };
    int fire_visited[1001][1001] = {0, };

    queue<pair<int, int> > jq;
    queue<pair<int, int> > fq;
    for (int i = 0; i < r; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++)
        {
            board[i][j] = s[j];
            jihoon_visited[i][j] = -1;
            fire_visited[i][j] = -1;

            if (board[i][j] == '*')
            {
                fq.push(make_pair(i, j));
                fire_visited[i][j] = 0;
            }
            if (board[i][j] == '@')
            {
                jq.push(make_pair(i, j));
                jihoon_visited[i][j] = 0;
            }
        }
    }

    while (!fq.empty())
    {
        auto cur = fq.front();
        fq.pop();

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if (nx < 0 || ny < 0 || nx >= r || ny >= c)
            {
                continue;
            }
            if (board[nx][ny] == '#' || fire_visited[nx][ny] != -1)
            {
                continue;
            }
            fq.push(make_pair(nx, ny));
            fire_visited[nx][ny] = fire_visited[cur.first][cur.second] + 1;
        }
    }

    while (!jq.empty())
    {
        auto cur = jq.front();
        jq.pop();

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if (nx < 0 || ny < 0 || nx >= r || ny >= c)
            {
                cout << jihoon_visited[cur.first][cur.second] + 1 << '\n';
                return;
            }
            if (jihoon_visited[nx][ny] != -1 || board[nx][ny] == '#')
            {
                continue;
            }
            if (fire_visited[nx][ny] != -1 && fire_visited[nx][ny] <= jihoon_visited[cur.first][cur.second] + 1)
            {
                continue;
            }

            jihoon_visited[nx][ny] = jihoon_visited[cur.first][cur.second] + 1;
            jq.push(make_pair(nx, ny));
        }
    }
    cout << "IMPOSSIBLE" << '\n';
}

int main() {

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        solution();
    }
}