#include <iostream>
#include <queue>
#include <utility>

using namespace std;

bool visited[1000][1000] = {};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int n;

bool dfs(int x, int y) {
    if (x == 1 || y == 1 || x == n || y == n) {
        return false;
    }

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < 1 || ny < 1 || nx > n || ny > n) {
            continue;
        }
        if (visited[nx][ny]) {
            continue;
        }
        visited[nx][ny] = true;
        if (!dfs(nx, ny)) {
            visited[nx][ny] = false;
            return true;
        }
        visited[nx][ny] = false;
    }
    return false;
}

int main() {

    // 홀수인 N * N 크기 격자에서 게임
    // (1, 1) ... (N, N)

    // 처음에 격자 정중앙 (n+1)/2, (n+1)/2 에서 시작
    // 자신의 턴에 말 상하좌우 중 한 칸만 이동 -> 이전에 말이 한 번이라도 있었으면 재방문 불가
    // 자신의 턴에 말을 움직이지 못하거나 자신의 턴이 시작할 때 말이 격자의 테두리에 위치한다면 진다
    // 테두리란 (1, N), (N, 1) 등 x혹은y가 1 또는 N인 경우

    // BFS 사용하고, visited 체크하면 될듯?



    cin >> n;

    // 첫 턴이 호반우, 다음 턴이 상우


    // 시작점부터 둬보자. 호반우 턴임
    // 이제부터 호반우는 1, 상우는 2, 시작점을 3, 빈칸은 0으로 표현하자


    // 직접 그려보니까 무조건 번갈아가면서 시계방향이던 반시계던 원을 그리면서 놔야 최적임

    // BFS 안되는 거 확인했으니까, 다른 방식 써봐야겠다

    int sp = (n + 1) / 2;
    visited[sp][sp] = true;

    // bool hobanwoo = dfs(sp, sp);
    
    if (n == 3) {
        cout << "Hobanwoo\n";
    } else {
        cout << "Sangho\n";
    }
}