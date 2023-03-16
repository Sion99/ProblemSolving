#include <iostream>

using namespace std;

int num[21];
int n, s;
int cnt = 0;

void dfs(int cur, int tot)
{
    if (cur == n)
    {
        if (tot == s)
            cnt++;
        return;
    }
    dfs(cur + 1, tot);
    dfs(cur + 1, tot + num[cur]);
}

int main()
{
    cin >> n >> s;
    for (int i = 0; i < n; i++)
        cin >> num[i];
    dfs(0, 0);
    if (s == 0)
        cnt--;
    cout << cnt << '\n';
}