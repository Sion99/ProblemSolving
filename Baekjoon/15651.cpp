#include <iostream>

using namespace std;

int n, m;
int number[8];

void dfs(int a)
{
	if (a == m)
	{
		for (int i = 0; i < m; i++)
		{
			cout << number[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++)
	{
		number[a] = i;
		dfs(a + 1);
	}
}

int main()
{
	cin >> n >> m;
	dfs(0);
}
