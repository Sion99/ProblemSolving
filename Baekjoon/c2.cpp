#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAX_N = 1000;
int N;
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int dp[MAX_N][MAX_N][2]; // 0: 호반우 차례, 1: 상호 차례

bool is_valid(int x, int y)
{
    return x >= 0 && x < N && y >= 0 && y < N;
}

bool is_edge(int x, int y)
{
    return x == 0 || x == N - 1 || y == 0 || y == N - 1;
}

int solve(int x, int y, int turn, vector<vector<bool>> &visited)
{
    if (is_edge(x, y))
        return turn ^ 1; // 현재 플레이어의 패배

    int &ret = dp[x][y][turn];
    if (ret != -1)
        return ret;

    bool can_move = false;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i], ny = y + dy[i];
        if (is_valid(nx, ny) && !visited[nx][ny])
        {
            can_move = true;
            visited[nx][ny] = true;
            if (solve(nx, ny, turn ^ 1, visited) == turn)
            {
                visited[nx][ny] = false;
                return ret = turn; // 현재 플레이어의 승리
            }
            visited[nx][ny] = false;
        }
    }

    if (!can_move)
        return ret = turn ^ 1; // 현재 플레이어의 패배
    return ret = turn ^ 1;     // 모든 움직임이 패배로 이어지면 현재 플레이어의 패배
}

int main()
{
    cin >> N;
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    memset(dp, -1, sizeof(dp));

    int start = N / 2;
    visited[start][start] = true;

    int result = solve(start, start, 0, visited);

    if (result == 0)
    {
        cout << "Hobanwoo" << endl;
    }
    else
    {
        cout << "Sangho" << endl;
    }
    return 0;
}