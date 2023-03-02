#include <vector>
#include <iostream>

using namespace std;

int main()
{
    string S;

    cin >> S;
    vector<int> v(26);
    for (int i = 0; i < S.size(); i++)
    {
        v[S[i] - 97] += 1;
    }
    for (int i = 0; i < 26; i++)
    {
        cout << v[i] << " ";
    }
}