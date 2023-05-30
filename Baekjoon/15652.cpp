#include <iostream>

using namespace std;

int n, m;
int board[9];

void dfs(int a)
{
	if (a == m)
	{
		for (int i = 0; i < m; i++)
		{
			cout << board[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++)
	{
		if (a == 0 || board[a - 1] <= i)
		{
			board[a] = i;
			dfs(a + 1);
		}
	}
}

int main()
{
	cin >> n >> m;
	dfs(0);
}
