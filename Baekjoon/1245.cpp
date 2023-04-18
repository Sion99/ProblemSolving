#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int board[100][70];
bool visited[100][70];
bool isPeak = true;

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

void bfs(int i, int j, int n, int m)
{
	queue<pair<int, int>> Q;
	Q.push({i, j});
	visited[i][j] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		for (int dir = 0; dir < 8; dir++)
		{
			int nx = cur.first + dx[dir];
			int ny = cur.second + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (board[cur.first][cur.second] < board[nx][ny])
				isPeak = false;
			if (visited[nx][ny] || board[cur.first][cur.second] != board[nx][ny])
				continue;
			Q.push({nx, ny});
			visited[nx][ny] = true;
		}
	}
}

int main()
{
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> board[i][j];
	int count = 0;
	queue<pair<int, int>> Q;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] != 0 && visited[i][j] == 0)
			{
				isPeak = true;
				Q.push({i, j});
				visited[i][j] = true;
				bfs(i, j, n, m);
				if (isPeak)
					count++;
			}
		}
	}
	cout << count << '\n';
}