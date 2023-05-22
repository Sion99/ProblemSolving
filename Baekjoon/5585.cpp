#include <iostream>

using namespace std;

int main()
{
	int n;
	int count = 0;
	int arr[5] = {500, 100, 50, 10, 5};
	cin >> n;
	n = 1000 - n;

	for (int i = 0; i < 5; i++)
	{
		count += (n / arr[i]);
		n = n % arr[i];
	}
	count += n;
	cout << count;
}
