#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[100001];
int t, cnt;

int where2Move(int x, int n)
{
	if (n == 0)
		return x - 1;
	else if (n == 1)
		return x + 1;
	else
		return 2 * x;
}


// 숨바꼭질 1과 다르게, 최단거리로 갈 수 있는 방법이 여러 개임을 세어야 한다.
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
		// 최단거리로 갈 수 있는 방법이 여러 개일 수 있으므로, pop한 뒤 visited 체크
		
		// 이미 최단거리로 도달한 경우가 있을 때
		if (cnt && cur.first == k && t == cur.second)
		{
			cnt++;
		}

		// 최초로 동생 위치에 도달한 경우
		if (!cnt && cur.first == k)
		{
			t = cur.second;
			cnt++;
		}

		for (int i = 0; i < 3; i++)
		{
			int next = where2Move(cur.first, i);
			if (next < 0 || next > 100001)
				continue;
			if (visited[next])
				continue;
			Q.push(make_pair(next, cur.second + 1));
		}
	}
}

int main()
{
	int n, k;
	cin >> n >> k;
	bfs(n, k);
	cout << t << '\n' << cnt;
	return 0;
}
