#include <iostream>
#include <queue>
#include <string>

using namespace std;

char board[251][251];
bool visited[251][251];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void checkFence(int r, int c)
{
	queue<pair<int, int> > Q;
	int wolf_total = 0;
	int sheep_total = 0;
	int wolf_temp = 0;
	int sheep_temp = 0;

	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (board[i][j] != '#' && visited[i][j] == false)
			{
				wolf_temp = 0;
				sheep_temp = 0;
				Q.push(make_pair(i, j));
				visited[i][j] = true;
				while (!Q.empty())
				{
					auto cur = Q.front();
					Q.pop();
					if (board[cur.first][cur.second] == 'v')
						wolf_temp++;
					else if (board[cur.first][cur.second] == 'k')
						sheep_temp++;
					for (int dir = 0; dir < 4; dir++)
					{
						int nx = cur.first + dx[dir];
						int ny = cur.second + dy[dir];
						if (nx < 0 || nx >= r || ny < 0 || ny >= c)
							continue;
						if (board[nx][ny] == '#' || visited[nx][ny])
							continue;
						Q.push(make_pair(nx, ny));
						visited[nx][ny] = true;
					}
				}
				// 펜스로 둘러쳐 진 공간에서 늑대와 양의 수를 센 다음
				// 어느 쪽이 더 많은 지 확인한 후 전체 숫자에 합산함
				if (wolf_temp >= sheep_temp)
					wolf_total += wolf_temp;
				else
					sheep_total += sheep_temp;
			}
		}
	}
	cout << sheep_total << ' ' << wolf_total;
}

int main()
{
	int r, c;
	cin >> r >> c;

	// 지도 입력받기.
	// 빈 공간이 '.', 울타리를 '#', 늑대를 'v', 양을 'k'라고 표현.
	for (int i = 0; i < r; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < c; j++)
		{
			board[i][j] = s[j];
		}
	}
	checkFence(r, c);
}
