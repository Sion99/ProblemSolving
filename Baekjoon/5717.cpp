#include <iostream>

using namespace std;

int main()
{
	int m, f;
	m = 1; f = 1;
	while (1)
	{
		cin >> m >> f;
		if (!m && !f)
			break;
		cout << m + f << '\n';
	}
}