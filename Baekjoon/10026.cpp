#include <iostream>
#include <queue>
#include <utility>
#include <string>

using namespace std;

char board[101][101];
bool visited[101][101];
bool visited2[101][101];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int main()
{
	int n;
	string str;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		for (int j = 0; j < n; j++)
			board[i][j] = str[j];
	}
	char c;
	int count = 0;
	int count2 = 0;
	queue<pair<int, int>> Q;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (visited[i][j] == 0)
			{
				c = board[i][j];
				Q.push({i, j});
				visited[i][j] = 1;
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
						if (board[nx][ny] != c || visited[nx][ny] == 1)
							continue;
						Q.push({nx, ny});
						visited[nx][ny] = 1;
					}
				}
				count++;
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (board[i][j] == 'G')
				board[i][j] = 'R';
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (visited2[i][j] == 0)
			{
				c = board[i][j];
				Q.push({i, j});
				visited2[i][j] = 1;
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
						if (board[nx][ny] != c || visited2[nx][ny] == 1)
							continue;
						Q.push({nx, ny});
						visited2[nx][ny] = 1;
					}
				}
				count2++;
			}
		}
	}
	cout << count << ' ' << count2 << '\n';
}