#include <iostream>

using namespace std;

int arr[1515];

int check_15gg(int n)
{
	if (n % 15 == 0)
		return 1;
	return 0;
}

int main()
{
	int n;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		if (i % 2 == 0)
			arr[i] = 1;
		else
			arr[i] = 5;
	}
}