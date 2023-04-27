#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct dslr{
	int num;
	string order;
} dslr;

bool visited[10001];
string table[10001];

char od[4] = {'D', 'S', 'L', 'R'};

bool compare(string a, string b)
{
	return (a.size() < b.size());
}

int DSLR(int n, char order)
{
	if (order == 'D')
		return ((2 * n) % 10000);
	else if (order == 'S')
	{
		if (n == 0)
			return (9999);
		else
			return (n - 1);
	}
	else if (order == 'L')
		return (n % 1000) * 10 + (n / 1000);
	else
		return (n % 10) * 1000 + (n / 10);
}

int main()
{
	int t, a, b;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> a >> b;
		queue<dslr> Q;
		vector<string> v;
		dslr temp;
		temp.num = a;
		temp.order = "";
		Q.push(temp);
		while (!Q.empty())
		{
			auto cur = Q.front();
			Q.pop();
			if (cur.num == b)
			{
				break;
			}
			dslr next[4];
			for (int i = 0; i < 4; i++)
			{
				next[i].num = DSLR(cur.num, od[i]);
				next[i].order = cur.order + od[i];
				if (!visited[next[i].num])
				{
					Q.push(next[i]);
					visited[next[i].num] = true;
					table[next[i].num] = next[i].order;
				}
			}
		}
		cout << table[b] << '\n';
	}
}