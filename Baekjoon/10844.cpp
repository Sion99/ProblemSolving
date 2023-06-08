#include <iostream>

using namespace std;

// 규칙
// 처음에 1 2 3 4 5 6 7 8 9에서 시작
// 자릿수가 하나씩 늘어가면서 각 자리에 해당하는 선택지에 1을 더한값과 1을 뺀 값, 두개를 덧붙일 수 있다
// 단, 끝 자리가 0인 경우에는 1을 더한 값 하나만 더해질 수 있다.

int stairs[101][10];

void getStairs()
{
	for (int i = 1; i < 10; i++)
	{
		stairs[1][i] = 1;
	}
	stairs[1][0] = 0;

	// i가 각 자리수 (N), j는 시작하는 숫자 (1, 2, 3 ...)
	for (int i = 2; i < 101; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (j == 0)
				stairs[i][j] = stairs[i - 1][j + 1] % 1000000000;
			else if (j == 9)
				stairs[i][j] = stairs[i - 1][j - 1] % 1000000000;
			else
				stairs[i][j] = (stairs[i - 1][j - 1] + stairs[i - 1][j + 1]) % 1000000000;
		}
	}
}

int main()
{
	int n;
	int ans = 0;
	cin >> n;
	getStairs();
	for (int i = 0; i < 10; i++)
	{
		ans = (ans + stairs[n][i]) % 1000000000;
	}
	cout << ans << '\n';
}
