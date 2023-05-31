#include <iostream>
#include <queue>

using namespace std;

int board[11][11];
bool visited[11][11];
int dice[6] = {1, 2, 3, 4, 5, 6};

int main()
{
	int n, m, x, y;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> x >> y;
		board[x / 10][x % 10] = y;
	}
	// 1 -> board[0][1]
	// 11 -> board[1][1];
	// 62 -> board[6][2];
	// 100 -> board[10][0];
	for (int i = 0; i < m; i++)
	{
		cin >> x >> y;
		board[x / 10][x % 10] = y;
	}
	queue<pair<int, int> > Q;
	Q.push(make_pair(1, 0));
	visited[0][1] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		visited[cur.first / 10][cur.first % 10] = true;
		if (cur.first == 100)
		{
			cout << cur.second;
			break;
		}
		for (int dir = 0; dir < 6; dir++)
		{
			int next = cur.first + dice[dir];
			if (next < 0 || next > 100)
				continue;
			if (visited[next / 10][next % 10])
				continue;
			while (board[next / 10][next % 10] != 0)
			{
				next = board[next / 10][next % 10];
			}
			Q.push(make_pair(next, cur.second + 1));
		}
	}
	return 0;
}
