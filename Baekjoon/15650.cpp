#include <iostream>

using namespace std;

int n, m;
int number[9];
bool visited[9];

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
		if (a == 0 || number[a - 1] <= i)
		{
			if (visited[i])
			continue;
			visited[i] = true;
			number[a] = i;
			dfs(a + 1);
			visited[i] = false;
		}
	}
}

int main()
{
	cin >> n >> m;
	dfs(0);
}
