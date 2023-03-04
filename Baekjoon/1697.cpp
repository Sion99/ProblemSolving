#include <iostream>
#include <queue>
// bfs는 신인가???
using namespace std;

int range[100001];
int visited[100001];

int main()
{
    int n, k;
    cin >> n >> k;
    queue<int> Q;
    visited[n] = 0;
    Q.push(n);
    while (!Q.empty())
    {
        int cur = Q.front();
        Q.pop();
        if (cur == k)
        {
            cout << visited[cur] << '\n';
            break;
        }
        int m[3] = {cur - 1, cur + 1, cur * 2};
        for (int i = 0; i < 3; i++)
        {
            if (m[i] < 0 || m[i] > 100000)
                continue;
            if (visited[m[i]] > 0)
                continue;
            visited[m[i]] = visited[cur] + 1;
            Q.push(m[i]);
        }
    }
}