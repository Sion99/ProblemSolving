#include <iostream>
#include <queue>
#include <string>

using namespace std;

int visited[1000][1000][11];
int board[1000][1000];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void bfs(int n, int m, int k)
{
	queue<pair<pair<int, int>, int> > Q;
	Q.push(make_pair(make_pair(0, 0), k));
	visited[0][0][k] = 1;
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
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (visited[nx][ny][cur.second])
				continue;
			// 벽이 존재하고, 부술 수 있는 기회가 있을 때
			if (board[nx][ny] == 1 && cur.second > 0 && visited[nx][ny][cur.second - 1] == 0)
			{
				Q.push(make_pair(make_pair(nx, ny), cur.second - 1));
				visited[nx][ny][cur.second - 1] = visited[cur.first.first][cur.first.second][cur.second] + 1;
			}

			// 벽이 존재하지 않을 때
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
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n, m, k;
	string s;
	cin >> n >> m >> k;
	// 지도 입력받기
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			board[i][j] = s[j] - '0';
		}
	}
	bfs(n, m, k);	// 지도에 이동한 거리 그리기
	int flag = 0;
	for (int i = 0; i <= k; i++)
	{
		if (visited[n - 1][m - 1][i] != 0)
		{
			cout << visited[n - 1][m - 1][i];
			flag = 1;
			break;
		}	
	}
	if (flag == 0)
		cout << -1;
	return 0;
}
