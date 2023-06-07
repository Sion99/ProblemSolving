#include <iostream>
#include <vector>

using namespace std;

int graph[101][101];

void floyd(int n, int m)
{
	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				if (i == j)
					continue;
				if (graph[i][k] != 0 && graph[k][j] != 0)
				{
					if (graph[i][j] == 0)
					{
						graph[i][j] = graph[i][k] + graph[k][j];
					}
					else
					{
						graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
					}
				}
			}
		}
	}
}

int main()
{
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		graph[a][b] = 1;
		graph[b][a] = 1;
	}
	floyd(n, m);
	int result = 999999;
	int kevin;
	for (int i = 1; i <= n; i++)
	{
		int bacon = 0;
		for (int j = 1; j <= n; j++)
		{
			bacon += graph[i][j];
		}
		if (result > bacon)
		{
			result = bacon;
			kevin = i;
		}
	}
	cout << kevin;
}