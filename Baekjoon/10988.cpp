#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	string s;
	cin >> s;
	string a = s;
	reverse(s.begin(), s.end());
	if (a == s)
		cout << 1;
	else
		cout << 0;
}