#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef struct node
{
	vector<int> vec;
} node;

node arr[100001];

int main()
{
	int n, m, r, u, v;
	cin >> n >> m >> r;
	for (int i = 0; i < m; i++)
	{
		cin >> u >> v;
		arr[u].vec.push_back(v);
		arr[v].vec.push_back(u);
	}
	for (int i = 0; i < n; i++)
	{
		
	}
}