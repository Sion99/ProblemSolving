#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int main() {

    // 1로 연결된 것이 그림
    // 그림의 개수, 가장 넓은 그림 넓이 출력

    int n, m;
    cin >> n >> m;

    int arr[n][m];
    int visited[n][m];

    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            visited[i][j] = 0;
        }
    }

    int cnt = 0;
    int max = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 1 && visited[i][j] == 0) {
                // 그림 시작점이니까 개수 += 1 해주고, BFS 시작
                queue<pair<int, int> > Q;
                cnt += 1;
                Q.push(make_pair(i, j));
                visited[i][j] = 1;
                int width = 0;

                while (!Q.empty()) {
                    auto cur = Q.front();
                    Q.pop();
                    width += 1;

                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                            continue;
                        }
                        if (arr[nx][ny] == 0 || visited[nx][ny] != 0) {
                            continue;
                        }
                        Q.push(make_pair(nx, ny));
                        visited[nx][ny] = 1;
                    }
                }
                if (width > max) {
                    max = width;
                }
            }
        }
    }
    cout << cnt << '\n' << max;
}