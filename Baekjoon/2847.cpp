#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 게임에는 총 N개의 레벨이 있고, 각 레벨을 클리어할 때 점수 부여
    // 레벨 점수 합으로 순위 결정
    // 특정 레벨 점수 감소시켜서 각 레벨별 점수 오름차순으로 (정렬 맞게 만들기)

    // 각 레벨별 점수 주어졌을 때 몇 번 감소시키면 오름차순 만족하는지?

    int n;
    cin >> n;

    vector<int> level_score;
    for (int i = 0; i < n; i++) {
        int score;
        cin >> score;
        level_score.push_back(score);
    }

    // 뒤로부터 시작해서 줄여가면 될듯?

    int last = level_score[n - 1];
    int sum = 0;
    for (int i = n - 2; i >= 0; i--) {
        int cnt = 0;
        while (level_score[i] >= last) {
            level_score[i]--;
            cnt++;
        }
        sum += cnt;
        last = level_score[i];
    }

    cout << sum << '\n';
}