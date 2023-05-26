#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[100001];
vector<int> v;

bool compare(vector<int> a, vector<int> b)
{
	return (a.size() < b.size());
}

int where2Move(int x, int n)
{
	if (n == 0)
		return x - 1;
	else if (n == 1)
		return x + 1;
	else
		return 2 * x;
}

// void bfs(int n, int k)
// {
// 	queue<pair<int, vector<int> > > Q;

// 	vector<int> ans;
// 	v.push_back(n);
// 	Q.push(make_pair(n, v));
// 	while (!Q.empty())
// 	{
// 		auto cur = Q.front();
// 		Q.pop();
// 		if (cur.first == k)
// 		{
// 			ans = cur.second;
// 			break;
// 		}
// 		for (int i = 0; i < 3; i++)
// 		{
// 			int next = where2Move(cur.first, i);
// 			if (next < 0 || next > 100000)
// 				continue;
// 			if (visited[next])
// 				continue;
// 			cur.second.push_back(next);
// 			Q.push(make_pair(next, cur.second));
// 			visited[next] = true;
// 		}
// 	}
// 	int length = ans.size() - 1;
// 	cout << length << '\n';
// 	for (int i = 0; i < ans.size(); i++)
// 	{
// 		cout << ans[i] << ' ';
// 	}
// }

void bfs(int n, int k)
{
	queue<pair<int, vector<int> > > Q;
	vector<int> ans;
	vector<vector<int> > vec; 
	v.push_back(n);

	Q.push(make_pair(n, v));
	visited[n] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		if (cur.first == k)
		{
			vec.push_back(cur.second);
		}
		for (int i = 0; i < 3; i++)
		{
			int next = where2Move(cur.first, i);
			vector<int> nx = cur.second;
			if (next < 0 || next > 100000)
				continue;
			if (visited[next])
				continue;
			nx.push_back(next);
			Q.push(make_pair(next, nx));
			visited[next] = true;
		}
	}
	sort(vec.begin(), vec.end(), compare);
	ans = vec[0];
	int length = ans.size() - 1;
	cout << length << '\n';
	for (int i = 0; i < ans.size(); i++)
	{
		cout << ans[i] << ' ';
	}
}

int main()
{
	int n, k;
	cin >> n >> k;
	bfs(n, k);
}
