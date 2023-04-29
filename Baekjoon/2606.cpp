#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

bool visited[101];

int main()
{
	int n, link, x, y;
	cin >> n >> link;
	vector <pair<int, int>> v;
	for (int i = 0; i < link; i++)
	{
		cin >> x >> y;
		if (x < y)
			v.push_back({x, y});
		else
			v.push_back({y, x});
	}
	queue<pair<int, int>> Q;
	visited[1] = true;
	int count = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i].first == 1)
		{
			Q.push(v[i]);
		}
	}
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		int next = cur.second;
		if (!visited[next])
		{
			visited[next] = true;
			count++;
		}
		for (int i = 0; i < v.size(); i++)
		{
			if (v[i].first == next)
			{
				Q.push(v[i]);
			}
		}
	}
	cout << count << '\n';
}