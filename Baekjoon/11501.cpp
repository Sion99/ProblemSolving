#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    // 매일 셋 중 하나
    // 1. 주식 1주 사기
    // 2. 원하는 만큼 주식 팔기
    // 3. 아무것도 안하기

    // 최대 이익 계산

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;

        vector<int> prices;
        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;

            prices.push_back(a);
        }

        // 가장 가까운 최댓값 지점 (극댓값) 까지 모으고, 판다
        // 팔았으면 다시 가장 가까운 최댓값 지점까지 모은다.

        int max_val = prices[n - 1];

        long long ans = 0;

        for (int i = n - 2; i >= 0; --i) {
            if (prices[i] > max_val) {
                max_val = prices[i];
            }
            ans += max_val - prices[i];
        }
        cout << ans << '\n';
    }
}