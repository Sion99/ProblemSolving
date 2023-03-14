#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    while (1)
    {
        getline(cin, s);
        if (s == "#")
            break;
        int len = s.size();
        int count = 0;
        for (int i = 0; i < len; i++)
        {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                count++;
            if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
                count++;
        }
        cout << count << '\n';
    }
}