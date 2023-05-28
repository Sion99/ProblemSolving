#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

// 공기와 한 면 이상 접촉한 칸(치즈)은 한 시간 뒤 녹는다.
// 치즈에 난 구멍은 초기에는 공기로 간주되지 않지만,
// 구멍이 치즈 외부와 접촉되는 순간 공기로 간주된다.

vector<pair<int, int> > checkAir(int n, int m, int hour)
{
	bool visited[101][101] = {false, };
	queue<pair<int, int> > Q;
	vector<pair<int, int> > res;
	Q.push(make_pair(0, 0));
	visited[0][0] = true;
	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		board[cur.first][cur.second] = hour;
		for (int dir = 0; dir < 4; dir++)
		{
			int nx = cur.first + dx[dir];
			int ny = cur.second + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (board[nx][ny] == -1)
			{
				res.push_back(make_pair(nx, ny));
				continue;
			}
			if (visited[nx][ny])
				continue;
			Q.push(make_pair(nx, ny));
			visited[nx][ny] = true;
		}
	}
	return (res);
}

void printArr(int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << board[i][j] << ' ';
		}
		cout << '\n';
	}
}

int main()
{
	int n, m, hour, last, survives;
	cin >> n >> m;
	
	// 치즈 위치 입력
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> board[i][j];
			if (board[i][j] == 1)
				board[i][j] = -1;
		}
	}
	hour = 1;
	last = 0;
	survives = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] == -1)
				survives++;
		}
	}
	while (1)
	{
		last = survives;
		auto cheese = checkAir(n, m, hour);
		for (int i = 0; i < cheese.size(); i++)
		{
			board[cheese[i].first][cheese[i].second] = hour;
		}
		survives = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (board[i][j] == -1)
					survives++;
			}
		}
		if (survives == 0)
		{
			cout << hour << '\n';
			cout << last << '\n';
			break;
		}
		hour++;
	}
}