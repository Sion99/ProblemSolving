#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec[1001];
bool dfs_check[1001];
bool bfs_check[1001];

// DFS
// 재귀를 사용해서 탐색
void dfs(int v)
{
	dfs_check[v] = true;
	cout << v << ' ';
	for (int i = 0; i < vec[v].size(); i++)
	{
		int next = vec[v][i];
		if (!dfs_check[next])
			dfs(next);
	}
}

// BFS
// 큐를 사용해서 탐색
void bfs(int v)
{
	queue<int> Q;
	Q.push(v);
	bfs_check[v] = true;
	while (!Q.empty())
	{
		int cur = Q.front();
		Q.pop();
		cout << cur << ' ';
		for (int i = 0; i < vec[cur].size(); i++)
		{
			int next = vec[cur][i];
			if (bfs_check[next])
				continue;
			bfs_check[next] = true;
			Q.push(next);
		}
	}
}

int main()
{
	int n, m, v;
	cin >> n >> m >> v;

	// 간선 입력받기
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a);
	}

	// 중요!! 간선 정렬하기!
	for (int i = 1; i <= n; i++)
	{
		sort(vec[i].begin(), vec[i].end());		
	}
	dfs(v);
	cout << '\n';
	bfs(v);
	cout << '\n';
	return 0;
}
