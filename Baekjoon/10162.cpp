#include <iostream>

using namespace std;

int main()
{
	int t;
	int count = 0;
	int arr[3] = {300, 60, 10};
	int num[3] = {0, 0, 0};
	cin >> t;
	if (t % 10 != 0)
	{
		cout << -1;
		return 0;
	}
	for (int i = 0; i < 3; i++)
	{
		num[i] = t / arr[i];
		t = t % arr[i];
	}
	for (int i = 0; i < 3; i++)
	{
		cout << num[i] << ' ';
	}
}
