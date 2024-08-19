#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
    // N개의 꽃, 같은 해 피어서 같은 해 진다
    // 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록
    // 심는 꽃들의 수를 가능한 적게
    // n개의 꽃 중에서 3월 1일부터 11월 30일까지 꽃이 한 가지 이상 유지가 되도록 하는 최소 꽃 개수

    int n;
    cin >> n;

    vector<pair<int, int> > flower;

    for (int i = 0; i < n; i++) {
        int sm, sd, em, ed;
        cin >> sm >> sd >> em >> ed;
        flower.push_back(make_pair(sm * 100 + sd, em * 100 + ed));
    }

    int t = 301;
    int ans = 0;

    while (t < 1201) {
        int nxt_t = t;

        for (int i = 0; i < n; i++) {
            if (flower[i].first <= t && flower[i].second > nxt_t) {
                nxt_t = flower[i].second;
            }
        }

        if (nxt_t == t) {
            cout << 0;
            return 0;
        }
        ans++;
        t = nxt_t;
    }

    cout << ans;

}