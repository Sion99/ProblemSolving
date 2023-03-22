#include <iostream>

typedef struct cost
{
	int r;
	int g;
	int b;
} cost;

cost arr[1001];

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].r >> arr[i].g >> arr[i].b;
	}
}