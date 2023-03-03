#include <iostream>
#include <stack>

using namespace std;

int main()
{
    string s;
    cin >> s;
    stack<char> stack;
    int count = 0;
    for (auto i : s)
    {
        if (i == '(')
        {
            stack.push('(');
        }
        else if (i == ')')
        {
            if (stack.top() == '(')
            {
                ;
            }
        }
    }
}