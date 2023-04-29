#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int t, x, y, dist, close, remain;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int count;
		cin >> x >> y;
		dist = y - x;
		close = sqrt(dist);
		count = close * 2 - 1;
		remain = dist - close * close;
		if (remain != 0)
		{
			if (remain <= close)
				count++;
			else
				count += 2;
		}
		cout << count << '\n';
	}
}