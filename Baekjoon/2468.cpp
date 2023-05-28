#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(int n, int level)
{
	queue<pair<int, int> > Q;
	bool visited[101][101] = {false, };
	int count = 0;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (board[i][j] > level && visited[i][j] == false)
			{
				Q.push(make_pair(i, j));
				visited[i][j] = true;
				while (!Q.empty())
				{
					auto cur = Q.front();
					Q.pop();
					for (int dir = 0; dir < 4; dir++)
					{
						int nx = cur.first + dx[dir];
						int ny = cur.second + dy[dir];
						if (nx < 0 || nx >= n || ny < 0 || ny >= n)
							continue;
						if (board[nx][ny] <= level)
							continue;
						if (visited[nx][ny])
							continue;
						Q.push(make_pair(nx, ny));
						visited[nx][ny] = true;
					}
				}
				count++;
			}
		}
	}
	return (count);
}

int main()
{
	int n, res;
	int max = 0;
	int ans = 0;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> board[i][j];
			if (board[i][j] > max)
				max = board[i][j];
		}
	}
	for (int i = 0; i < max; i++)
	{
		res = bfs(n, i);
		if (res > ans)
			ans = res;
	}
	cout << ans;
}