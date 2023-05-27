#include <iostream>
#include <queue>
#include <string>

using namespace std;

bool visited[100000001];

typedef struct node
{
	int num;
	string order;
} node;

int	where2Move(int s, int i)
{
	if (i == 0)
		return (2 * s);
	else if (i == 1)
		return (0);
	else if (i == 2)
		return (s * s);
	else
		return (1);
}

void bfs(int s, int t)
{
	queue<node> Q;
	vector<string> ans;
	node first;
	first.num = s;
	first.order = "";
	Q.push(first);

	while (!Q.empty())
	{
		auto cur = Q.front();
		Q.pop();
		visited[cur.num] = true;
		if (cur.num == t)
		{
			ans.push_back(cur.order);
		}
		for (int i = 0; i < 4; i++)
		{

		}
	}
}


int main()
{
	int s, t;
	cin >> s >> t;
	bfs(s, t);
}
