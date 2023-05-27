#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<pair<int, int> > parents[1001];
vector<pair<int, int> > child[1001];

int bfs(int a, int b)
{
	bool visited[1001] = {false, };
	queue<pair<int, int> > Q;
	Q.push(make_pair(a, 0));
	visited[a] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		if (cur.first == b)
			return cur.second;
		for (int i = 0; i < parents[a].size(); i++)
		{
			int next = parents[a][i].first;
			cur.second += parents[a][i].second;
			if (visited[next])
				continue;
			Q.push(make_pair(next, cur.second));
			visited[next] = true;
		}
		for (int i = 0; i < child[a].size(); i++)
		{
			int next = child[a][i].first;
			cur.second += child[a][i].second;
			if (visited[next])
				continue;
			Q.push(make_pair(next, cur.second));
			visited[next] = true;
		}
	}
	return 0;
}

int main()
{
	int n, m, a, b, len, ans;
	cin >> n >> m;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> a >> b >> len;
		parents[a].push_back(make_pair(b, len));
		child[b].push_back(make_pair(a, len));
	}
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b;
		ans = bfs(a, b);
		cout << ans << '\n';
	}
}
