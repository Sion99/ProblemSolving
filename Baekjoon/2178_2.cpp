#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
bool visited[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(int n, int m)
{
	int res = 0;
	queue<pair<pair<int, int>, int> > Q;
	Q.push(make_pair(make_pair(0, 0), 1));
	visited[0][0] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();

		// 미로의 끝에 도달하면 탐색 종료
		if (cur.first.first == n - 1 && cur.first.second == m - 1)
		{
			res = cur.second;
			break;
		}
		for (int dir = 0; dir < 4; dir++)
		{
			int nx = cur.first.first + dx[dir];
			int ny = cur.first.second + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (board[nx][ny] == 0)
				continue;
			if (visited[nx][ny])
				continue;
			Q.push(make_pair(make_pair(nx, ny), cur.second + 1));
			visited[nx][ny] = true;
		}
	}
	return (res);
}

int main()
{
	int n, m, ans;
	cin >> n >> m;
	// 지도 입력받기
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			board[i][j] = s[j] - '0';
		}
	}
	ans = bfs(n, m);
	cout << ans;
	return 0;
}
