#include <iostream>

using namespace std;

int main() {
    // n개의 정수 임의의 수열
    // 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합

    // 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 수열 있을 때
    // 12 + 21 = 33 정답

    int n;
    cin >> n;

    int arr[100001] = {0, };
    int dp[100001] = {0, };
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    dp[1] = arr[1];

    int mx = dp[1];

    for (int i = 2; i <= n; i++)
    {
        dp[i] = max(dp[i - 1] + arr[i], arr[i]);
        mx = max(mx, dp[i]);
    }

    cout << mx;
}