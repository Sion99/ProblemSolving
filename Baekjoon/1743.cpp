#include <iostream>
#include <queue>

using namespace std;

int board[101][101];
bool visited[101][101];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

// 가장 큰 음식물 크기 찾아내기
// 음식물을 발견할 때마다 bfs로 주위 음식물을 다 찾은 다음,
// 기존 최댓값과 크기를 비교하여 갱신한다.
int	findBiggest(int n, int m)
{
	queue<pair<int, int> > Q;
	int biggest = 0;
	int count = 0;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			if (board[i][j] == 1 && visited[i][j] == false)
			{
				count = 0;
				Q.push(make_pair(i, j));
				visited[i][j] = true;
				while(!Q.empty())
				{
					auto cur = Q.front();
					Q.pop();
					count++;
					for (int dir = 0; dir < 4; dir++)
					{
						int nx = cur.first + dx[dir];
						int ny = cur.second + dy[dir];
						
						if (nx < 1 || nx > n || ny < 1 || ny > m)
							continue;
						if (board[nx][ny] == 0 || visited[nx][ny])
							continue;
						Q.push(make_pair(nx, ny));
						visited[nx][ny] = true;
					}
				}
				biggest = max(count, biggest);
			}
		}
	}
	return biggest;
}

int main()
{
	int n, m, k, r, c, ans;
	cin >> n >> m >> k;

	// 음식물 위치 입력받아서 지도에 저장.
	// 음식물은 1, 빈 공간은 0으로 표시
	for (int i = 0; i < k; i++)
	{
		cin >> r >> c;
		board[r][c] = 1;
	}

	// 가장 큰 음식물 찾기!
	ans = findBiggest(n, m);
	cout << ans << '\n';
	return 0;
}
