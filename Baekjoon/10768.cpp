#include <iostream>

using namespace std;

int main()
{
	int m, d;
	cin >> m >> d;
	if (m > 2)
		cout << "After";
	else
	{
		if (m == 2)
		{
			if (d < 18)
				cout << "Before";
			else if (d == 18)
				cout << "Special";
			else
				cout << "After";
		}
		else
		{
			cout << "Before";
		}
	}
}