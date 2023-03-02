#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> stack;
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
            stack.push(num);
        }
        else if (s == "top")
        {
            if (stack.size() != 0)
                cout << stack.top() << '\n';
            else
                cout << "-1\n";
        }
        else if (s == "size")
        {
            cout << stack.size() << '\n';
        }
        else if (s == "pop")
        {
            if (stack.size() != 0)
            {
                cout << stack.top() << '\n';
                stack.pop();
            }
            else
                cout << "-1\n";
        }
        else
        {
            if (stack.size() == 0)
            {
                cout << "1\n";
            }
            else
            {
                cout << "0\n";
            }
        }
    }
}