#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> q;
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        if (s == "push")
        {
            int num;
            cin >> num;
            q.push(num);
        }
        else if (s == "pop")
        {
            if (q.size() == 0)
            {
                cout << "-1\n";
            }
            else
            {
                cout << q.front() << '\n';
                q.pop();
            }
        }
        else if (s == "size")
        {
            cout << q.size() << '\n';
        }
        else if (s == "empty")
        {
            if (q.empty())
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if (s == "front")
        {
            if (q.empty())
                cout << "-1\n";
            else
                cout << q.front() << '\n';
        }
        else
        {
            if (q.empty())
                cout << "-1\n";
            else
                cout << q.back() << '\n';
        }
    }
}