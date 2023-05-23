#include <iostream>
#include <queue>
#include <utility>
#include <string>

using namespace std;

int visited[1000][1000][2];
int board[1000][1000];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void bfs(int n, int m)
{
	queue<pair<pair<int, int>, int> > Q;
	Q.push(make_pair(make_pair(0, 0), 1));
	visited[0][0][1] = 1;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		if (cur.first.first == n - 1 && cur.first.second == m - 1)
			break;
		for (int dir = 0; dir < 4; dir++)
		{
			int nx = cur.first.first + dx[dir];
			int ny = cur.first.second + dy[dir];
			// 맵 범위 초과하는 점에 대해서 무시
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			// 벽이 존재하고, 부술 수 있는 기회가 있을 때
			if (board[nx][ny] == 1 && cur.second == 1)
			{
				Q.push(make_pair(make_pair(nx, ny), 0));
				visited[nx][ny][0] = visited[cur.first.first][cur.first.second][1] + 1;
			}
			// 벽이 존재하지 않을때
			else if (board[nx][ny] == 0 && visited[nx][ny][cur.second] == 0)
			{
				Q.push(make_pair(make_pair(nx, ny), cur.second));
				visited[nx][ny][cur.second] = visited[cur.first.first][cur.first.second][cur.second] + 1;
			}
		}
	}
}

int main()
{
	int n, m;
	cin >> n >> m;
	
	// 맵 입력받기
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			board[i][j] = s[j] - '0';
		}
	}
	bfs(n, m);	// 지도에 이동한 거리 그리기
	if (visited[n - 1][m - 1][0] == 0 && visited[n - 1][m - 1][1] == 0)
		cout << -1;
	else
	{
		if (visited[n - 1][m - 1][0] != 0)
			cout << visited[n - 1][m - 1][0];
		else
			cout << visited[n - 1][m - 1][1];
	}
	return 0;
}
