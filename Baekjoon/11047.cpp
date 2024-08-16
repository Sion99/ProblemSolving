#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b) {
    return a > b;
}

int main() {
    // N 종류 동전
    // 동전을 적절히 사용해서 합 K 만들기

    int N, K;
    cin >> N >> K;

    vector<int> v;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end(), compare);

    int curr = K;
    int cnt = 0;
    while (curr != 0) {
        for (int i = 0; i < N; i++) {
            if (curr / v[i] > 0) {
                cnt += curr / v[i];
                curr = curr % v[i];
            }
        }
    }
    cout << cnt;
}