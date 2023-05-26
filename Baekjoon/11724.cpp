#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> vec[1001];
bool check[1001];

void bfs(int n)
{
	queue<int> Q;
	Q.push(n);
	while (!Q.empty())
	{
		int cur = Q.front();
		Q.pop();
		for (int i = 0; i < vec[cur].size(); i++)
		{
			int next = vec[cur][i];
			if (check[next])
				continue;
			check[next] = true;
			Q.push(next);
		}
	}
}

int main()
{
	int n, m, u, v;
	cin >> n >> m;
	// 간선 양 끝점 입력받아서 각각 연결점 추가해주기
	for (int i = 0; i < m; i++)
	{
		cin >> u >> v;
		vec[u].push_back(v);
		vec[v].push_back(u);
	}
	int count = 0;
	// 모든 정점에 대하여 bfs 탐색 시작
	for (int i = 1; i <= n; i++)
	{
		if (check[i] == false)
		{
			bfs(i);
			count++;
		}
	}
	cout << count;
}
