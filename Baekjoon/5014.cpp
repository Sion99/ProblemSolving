#include <iostream>
#include <queue>
#include <utility>

using namespace std;

bool visited[1000001];

int main()
{
	int f, s, g, u, d;
	cin >> f >> s >> g >> u >> d;
	queue<pair<int, int>> Q;
	int arr[2] = {u, -d};
	visited[s] = true;
	Q.push({s, 0});
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		if (cur.first == g)
		{
			cout << cur.second;
			return (0);
		}
		for (int i = 0; i < 2; i++)
		{
			int next = cur.first + arr[i];
			if (next < 1 || next > f)
				continue;
			if (visited[next])
				continue;
			visited[next] = true;
			Q.push({next, cur.second + 1});
		}
	}
	cout << "use the stairs\n";
}
