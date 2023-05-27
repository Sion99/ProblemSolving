#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> parents[101];
vector<int> child[101];
bool visited[101];

int bfs(int a, int b)
{
    queue<pair<int, int> > Q;
    Q.push(make_pair(a, 0));
    visited[a] = true;
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        if (cur.first == b)
            return cur.second;
        for (int i = 0; i < parents[cur.first].size(); i++)
        {
            int next = parents[cur.first][i];
            if (visited[next])
                continue;
            Q.push(make_pair(next, cur.second + 1));
            visited[next] = true;
        }
        for (int i = 0; i < child[cur.first].size(); i++)
        {
            int next = child[cur.first][i];
            if (visited[next])
                continue;
            Q.push(make_pair(next, cur.second + 1));
            visited[next] = true;
        }
    }
    return -1;
}

int main()
{
    int n, a, b, m, x, y, ans;
    cin >> n >> a >> b >> m;
    for (int i = 0; i < m; i++)
    {
        // x는 y의 부모
        // y는 x의 자식
        cin >> x >> y;
        parents[x].push_back(y);
        child[y].push_back(x);
    }
    ans = bfs(a, b);
    cout << ans;
    return 0;
}
