#include <iostream>

using namespace std;

int main()
{
	int min[4];
	int man[4];

	int minmax = 0;
	int manmax = 0;

	for (int i = 0; i < 4; i++)
	{
		cin >> min[i];
		minmax += min[i];
	}
	for (int i = 0; i < 4; i++)
	{
		cin >> man[i];
		manmax += man[i];
	}
	if (minmax > manmax)
		cout << minmax;
	else
		cout << manmax;

}