#include <queue>
#include <vector>

using namespace std;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    queue<pair<int, int> > Q;
    int visited[101][101];
    for (int i = 0; i < maps.size(); i++)
    {
        for (int j = 0; j < maps[0].size(); j++)
        {
            visited[i][j] = -1;
        }
    }
    Q.push(make_pair(0, 0));
    visited[0][0] = 1;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if (nx < 0 || nx >= maps.size() || ny < 0 || ny >= maps[0].size())
                continue;
            if (maps[nx][ny] == 0)
                continue;
            if (visited[nx][ny] != -1)
                continue;
            Q.push(make_pair(nx, ny));
            visited[nx][ny] = visited[cur.first][cur.second] + 1;
        }
    }
    answer = visited[maps.size() - 1][maps[0].size() - 1];
    return answer;
}
