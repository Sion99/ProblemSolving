#include <iostream>
#include <queue>
#include <string>

using namespace std;

char board[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};


// char c를 받아서
// c와 동일한 문자들을 확인함
int bfs(int n, int m, char c)
{
	bool visited[101][101] = {false, };
	queue<pair<int, int> > Q;
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] == c && visited[i][j] == false)
			{
				int count = 0;
				Q.push(make_pair(i, j));
				visited[i][j] = true;
				while (!Q.empty())
				{
					auto cur = Q.front();
					Q.pop();
					count++;
					for (int dir = 0; dir < 4; dir++)
					{
						int nx = cur.first + dx[dir];
						int ny = cur.second + dy[dir];
						if (nx < 0 || nx >= n || ny < 0 || ny >= m)
							continue;
						if (visited[nx][ny] || board[nx][ny] != c)
							continue;
						Q.push(make_pair(nx, ny));
						visited[nx][ny] = true;
					}
				}
				sum += (count * count);
			}
		}
	}
	return sum;
}

int main()
{
	int n, m, alias, enemy;
	cin >> m >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			board[i][j] = s[j];
		}
	}
	alias = bfs(n, m, 'W');
	enemy = bfs(n, m, 'B');
	cout << alias << ' ' << enemy;
}
