#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;
    if (a.size() >= b.size())
        cout << "go\n";
    else
        cout << "no\n";
}