#include <iostream>
#include <list>

using namespace std;

int main()
{
    string s;
    cin >> s;
    list<char> li;
    for (auto c : s)
    {
        li.push_back(c);
    }
    auto cursor = li.end();
    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        char order;
        cin >> order;
        if (order == 'L')
        {
            if (cursor != li.begin())
                cursor--;
        }
        else if (order == 'D')
        {
            if (cursor != li.end())
                cursor++;
        }
        else if (order == 'B')
        {
            if (cursor != li.begin())
            {
                cursor--;
                cursor = li.erase(cursor);
            }
        }
        else
        {
            char c;
            cin >> c;
            li.insert(cursor, c);
        }
    }
    for (auto i : li)
    {
        cout << i;
    }
}