#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    string temp = "";
    string s = "0123456789ABCDEF";
    vector<string> v;
    if (m == 0)
    {
        cout << "0\n";
        return 0;
    }
    while (m != 0)
    {
        temp = s[(m % n)];
        v.push_back(temp);
        m /= n;
    }
    reverse(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
        cout << v[i];
    cout << '\n';
}