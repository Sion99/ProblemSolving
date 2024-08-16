#include <iostream>
#include <queue>
#include <utility>
#include <string>

using namespace std;

int main() {

    int N, M;
    cin >> N >> M;

    int board[N][M];
    int visited[N][M];
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++) {
            board[i][j] = s[j] - '0';
            visited[i][j] = 0;
        }
    }

    queue<pair<int, int> > Q;
    visited[0][0] = 1;
    Q.push(make_pair(0, 0));

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        if (cur.first == N - 1 && cur.second == M - 1) {
            break;
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                continue;
            }
            if (board[nx][ny] == 0 || visited[nx][ny] != 0) {
                continue;
            }
            Q.push(make_pair(nx, ny));
            visited[nx][ny] = visited[cur.first][cur.second] + 1;
        }
    }
    cout << visited[N - 1][M - 1] << '\n';
}