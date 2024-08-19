#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[1001] = {0, };
    int dp[1001] = {0, };

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    dp[1] = arr[1];
    int mx = dp[1];

    // for (int i = 2; i <= n; i++) {
    //     if (arr[i] > arr[i - 1]) {
    //         dp[i] = max(dp[i - 1] + arr[i], arr[i]);
    //         mx = max(mx, dp[i]);
    //     }
    // }

    for (int i = 1; i <= n; i++) {
        dp[i] = arr[i];
        for (int j = 1; j < i; j++) {
            if (arr[j] < arr[i] && dp[i] < dp[j] + arr[i]) {
                dp[i] = dp[j] + arr[i];
            }
        }
        mx = max(mx, dp[i]);
    }
    cout << mx;
}