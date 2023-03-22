#include <iostream>
#include <queue>

using namespace std;

int board[100001];
bool visited[100001];

int main()
{
	int n;
	cin >> n;
	Q.push(n);
	visited[n] = 1;
	int mn = 99999999;
	int count = 0;
	while (!Q.empty())
	{
		int cur = Q.front();
		Q.pop();
		count++;
		int next;
		if (cur % 3 == 0 && visited[cur / 3] == 0)
		{
			next = cur / 3;
			board[next] = board[cur] + 1;
			visited[next] = 1;
			Q.push(next);
		}
		if (cur % 2 == 0 && visited[cur / 2] == 0)
		{
			next = cur / 2;
			board[next] = board[cur] + 1;
			visited[next] = 1;
			Q.push(next);
		}
		if (visited[cur - 1] == 0)
		{
			next = cur - 1;
			board[next] = board[cur] + 1;
			visited[next] = 1;
			Q.push(next);
		}
	}
}