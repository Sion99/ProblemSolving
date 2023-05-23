#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(int i, int j)
{
	return j < i;
}

int main()
{
	string n;
	cin >> n;
	vector<int> arr;
	for (int i = 0; i < n.size(); i++)
		arr.push_back(n[i] - '0');
	if (count(arr.begin(), arr.end(), 0) == 0)
	{
		cout << -1;
		return 0;
	}
	int sum = 0;
	sort(arr.begin(), arr.end(), compare);
	for (int i = 0; i < arr.size(); i++)
	{
		sum += arr[i];
	}
	if (sum % 3 == 0)
	{
		for (int i = 0; i < arr.size(); i++)
		{
			cout << arr[i];
		}
	}
	else
	{
		cout << -1;
	}
}
