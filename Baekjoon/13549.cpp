#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[100001];

int where2Move(int x, int n)
{
	if (n == 0)
		return x - 1;
	else if (n == 1)
		return x + 1;
	else
		return 2 * x;
}

void bfs(int n, int k)
{
	queue<pair<int, int> > Q;
	vector<int> v;
	int ans = 0;

	Q.push(make_pair(n, 0));
	visited[n] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		visited[cur.first] = true;
		if (cur.first == k)
		{
			v.push_back(cur.second);
		}
		for (int i = 0; i < 3; i++)
		{
			int next = where2Move(cur.first, i);
			if (next < 0 || next > 100000)
				continue;
			if (visited[next])
				continue;
			if (i == 0 || i == 1)
				Q.push(make_pair(next, cur.second + 1));
			else
				Q.push(make_pair(next, cur.second));
		}
	}
	sort(v.begin(), v.end());
	cout << v[0];
}


int main()
{
	int n, k;
	cin >> n >> k;
	bfs(n, k);
}
