#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int dx[4] = {1, 2, -1, -2};
int dy[4] = {2, 1, -1, -2};

int main()
{
    int t, l;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> l;
        int board[301][301] = {};
        int visited[301][301];
        for (int j = 0; j < l; j++)
            for (int k = 0; k < l; k++)
                visited[j][k] = -1;
        int x, y, ox, oy;
        cin >> x >> y;
        queue<pair<int, int>> Q;
        Q.push({x, y});
        visited[x][y] = 0;
        cin >> ox >> oy;
        while (!Q.empty())
        {
            auto cur = Q.front();
            Q.pop();
            if (cur.first == ox && cur.second == oy)
            {
                cout << visited[cur.first][cur.second] << '\n';
                break;
            }
            pair<int, int> dir[8];
            dir[0] = {cur.first + 1, cur.second + 2};
            dir[1] = {cur.first + 2, cur.second + 1};
            dir[2] = {cur.first + 2, cur.second - 1};
            dir[3] = {cur.first + 1, cur.second - 2};
            dir[4] = {cur.first - 1, cur.second - 2};
            dir[5] = {cur.first - 2, cur.second - 1};
            dir[6] = {cur.first - 2, cur.second + 1};
            dir[7] = {cur.first - 1, cur.second + 2};
            for (int j = 0; j < 8; j++)
            {
                if (dir[j].first < 0 || dir[j].first >= l || dir[j].second < 0 || dir[j].second >= l)
                    continue;
                if (visited[dir[j].first][dir[j].second] >= 0)
                    continue;
                Q.push(dir[j]);
                visited[dir[j].first][dir[j].second] = visited[cur.first][cur.second] + 1;
            }
        }
    }
}