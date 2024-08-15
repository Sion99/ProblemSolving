#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // std::find를 사용하기 위해 필요

using namespace std;

bool compare(string a, string b)
{
    if (a.size() != b.size())
    {
        return a.size() < b.size();
    }
    else
    {
        return a < b;
    }
}

int main()
{
    int N;
    cin >> N;

    vector<string> v;

    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        auto idx = find(v.begin(), v.end(), str);
        if (idx == v.end())
        {
            v.push_back(str);
        }
    }

    sort(v.begin(), v.end(), compare);

    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }

    return 0;
}
