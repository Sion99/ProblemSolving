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

    int mx = 0;

    for (int i = 1; i <= n; i++) {
        dp[i] = 1;
        for (int j = i - 1; j >= 1; j--) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        mx = max(mx, dp[i]);
    }
    cout << mx;

}