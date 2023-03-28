#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[101][101];
int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};
vector<int> v;

void bfs(int a, int b, int m, int n)
{
    queue<pair<int, int>> Q;
    Q.push({a, b});
    visited[a][b] = 1;
    int count = 1;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.second + dx[dir];
            int ny = cur.first + dy[dir];
            if (nx < n && nx >= 0 && ny < m && ny >= 0){
                if(!visited[ny][nx]){
                    Q.push({ny, nx});
                    visited[ny][nx] = 1;
                    count++;
                }
            } 
        }
    }
    v.push_back(count);
}

int main()
{
    int total = 0;
    int m, n, k;
    int sx, sy, ex, ey;
    cin >> m >> n >> k;

    for (int i = 0; i < k; i++)
    {
        cin >> sx >> sy >> ex >> ey;
        for (int r = sy; r < ey; r++)
        {
            for (int l = sx; l < ex; l++)
            {
                visited[r][l] = 1;
            }
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                bfs(i, j, m, n);
                total++;
            }
        }
    }
    cout << total << '\n';
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << ' ';
    cout << '\n';
}