#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin >> n >> m;
    map<string, int> mm;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        mm.insert({s, 1});
    }
    int count = 0;
    for (int i = 0; i < m; i++)
    {
        string s;
        cin >> s;
        if (map[s] == 0)
            continue;
        count++;
    }
    cout << count << '\n';
}