#include <iostream>
#include <queue>

using namespace std;

int board[1001][1001];
int changed[1001][1001];
bool visited[1001][1001];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
	int n, m;
	cin >> n >> m;
	queue<pair<pair<int, int>, int> > Q;
	// N x M 지도 입력
	// 0은 벽, 1은 빈 공간, 2는 목표지점
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			// 전처리 단계
			// changed 배열을 미리 수정함으로써
			// 문제 조건에 부합하게 한다
			cin >> board[i][j];
			if (board[i][j] == 1)
			{
				changed[i][j] = -1;
			}
			if (board[i][j] == 2)
			{
				Q.push(make_pair(make_pair(i, j), 0));
				visited[i][j] = true;
			}
		}
	}
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		int x = cur.first.first;
		int y = cur.first.second;
		changed[x][y] = cur.second;
		for (int dir = 0; dir < 4; dir++)
		{
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (visited[nx][ny] || board[nx][ny] == 0)
				continue;
			Q.push(make_pair(make_pair(nx, ny), cur.second + 1));
			visited[nx][ny] = true;
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << changed[i][j] << ' ';
		}
		cout << '\n';
	}
}
