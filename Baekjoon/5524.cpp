#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < s.size(); j++)
		{
			if (s[j] >= 'A' && s[j] <= 'Z')
				s[j] += 32;
		}
		cout << s << '\n';
	}
}
