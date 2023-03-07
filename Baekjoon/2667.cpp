#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>
// 조건 잘 확인하기!!!
using namespace std;

int board[26][26];
int visited[26][26];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int n;
    cin >> n;
    int group = 0;
    int sum;
    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++)
        {
            board[i][j] = s[j] - 48;
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (board[i][j] == 0 || visited[i][j])
                continue;
            group++;
            queue<pair<int, int>> Q;
            visited[i][j] = 1;
            Q.push({i, j});
            sum = 0;
            while (!Q.empty())
            {
                sum++;
                pair<int, int> cur = Q.front();
                Q.pop();
                for (int dir = 0; dir < 4; dir++)
                {
                    int nx = cur.first + dx[dir];
                    int ny = cur.second + dy[dir];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                        continue;
                    if (visited[nx][ny] || board[nx][ny] != 1)
                        continue;
                    visited[nx][ny] = 1;
                    Q.push({nx, ny});
                }
            }
            v.push_back(sum);
        }
    }
    cout << group << '\n';
    sort(v.begin(), v.end());
    for (auto i = 0; i < v.size(); i++)
        cout << v[i] << '\n';
}