#include <iostream>

using namespace std;

int main() {
    // 거스름돈 동전 개수 최소로 주기

    int T;
    cin >> T;

    // 쿼터 (0.25)
    // 다임 (0.10)
    // 니켈 (0.05)
    // 페니 (0.01)
    // 편의성 100을 곱하자

    // 25, 10, 5, 1
    for (int i = 0; i < T; i++) {
        int num;
        int arr[4] = {25, 10, 5, 1};
        int cnt[4] = {0, 0, 0, 0};
        cin >> num;

        while (num != 0) {
            for (int i = 0; i < 4; i++) {
                cnt[i] += (num / arr[i]);
                num %= arr[i];
            }
        }

        for (int i = 0; i < 4; i++) {
            cout << cnt[i] << ' ';
        }
        cout << '\n';


    }
}