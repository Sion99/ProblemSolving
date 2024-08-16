#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) {
        return a.second > b.second;
    } else {
        return a.first > b.first;
    }
}

int main() {

    // 1차, 2차
    // 다른 지원자와 비교했을 때 1차 또는 2차가 다른 지원자보다 떨어지지 않아야함
    // 다른 지원자와 비교했을 때 1차 2차 모두 낮으면 탈락
    // 이런 조건 만족하면서 최대 채용 인원 수
    // 일단 탈락자만 줄여봐 -> 1, 2차 꼴등은 탈락

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        vector<pair<int, int> > v;

        for (int j = 0; j < N; j++) {
            int a, b;
            cin >> a >> b;
            v.push_back(make_pair(a, b));
        }

        sort(v.begin(), v.end(), compare);

        for (auto x : v) {
            cout << x.first << ' ' << x.second << '\n';
        }
    }

}