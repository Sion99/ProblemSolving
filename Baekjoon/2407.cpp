#include <iostream>
#include <vector>

using namespace std;

long long ans = 0;

void comb(int n, int m, vector<int> arr, int cnt)
{
    if (arr.size() == m)
    {
        ans++;
        return;
    }
    for (int i = cnt; i <= n; i++)
    {
        if (arr.size() < m)
        {
            arr.push_back(i);
            comb(n, m, arr, cnt + 1);
            arr.pop_back();
        }
    }
}

int main()
{
    int n, m;
    vector<int> arr;

    cin >> n >> m;
    comb(n, m, arr, 1);
    cout << ans << endl;
    return 0;
}