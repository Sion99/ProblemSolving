#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
int visited[101][101][2];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
	int n, m, t;
	cin >> n >> m >> t;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> board[i][j];
		}
	}
	// 앞의 pair는 각각 x, y 좌표
	// 뒤의 int는 '그람' 보유 여부
	queue<pair<pair<int, int>, int> > Q;
	Q.push(make_pair(make_pair(0, 0), 0));
	visited[0][0][0] = 0;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		if (visited[cur.first.first][cur.first.second][cur.second] > t)	// 시간 초과했을 때
			continue;
		if (cur.first.first == n - 1 && cur.first.second == m - 1)
		{
			cout << visited[n - 1][m - 1][cur.second];
			return 0;
		}
		if (board[cur.first.first][cur.first.second] == 2)	// '그람'이 있는 칸에 방문했다면
		{
			cur.second = 1;
		}
		for (int dir = 0; dir < 4; dir++)
		{
			int nx = cur.first.first + dx[dir];
			int ny = cur.first.second + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (cur.second == 1)	// '그람'을 획득했을 때
			{
				if (visited[nx][ny][1] > 0)
					continue;
				Q.push(make_pair(make_pair(nx, ny), 1));
				if (visited[cur.first.first][cur.first.second][1] == 0)
					visited[nx][ny][1] = visited[cur.first.first][cur.first.second][0] + 1;
				else
					visited[nx][ny][1] = visited[cur.first.first][cur.first.second][1] + 1;
			}
			else	// '그람'이 없을 때
			{
				if (board[nx][ny] == 1)
					continue;
				if (visited[nx][ny][0] > 0)
					continue;
				Q.push(make_pair(make_pair(nx, ny), 0));
				visited[nx][ny][0] = visited[cur.first.first][cur.first.second][0] + 1;
			}
		}
	}
	cout << "Fail";
	return 0;
}
