#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// ATM에 N명 사람 줄 1~N번
// Pi 분 소요
// 각 사람이 돈을 인출하는데 걸리는 소요시간 최소화

int main() {

    // 소요시간 적은 순서대로 정렬해보자

    int N;
    cin >> N;

    vector<int> v;
    for (int i = 0; i < N; i++) {
        int p;
        cin >> p;
        v.push_back(p);
    }
    sort(v.begin(), v.end());

    int sum = 0;
    for (int i = 0; i < N; i++) {
        int temp = 0;
        for (int j = 0; j < i; j++) {
            temp += v[j];
        }
        temp += v[i];
        sum += temp;
    }
    cout << sum;
}