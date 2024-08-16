#include <iostream>

using namespace std;

int main() {
    // 사탕가게 설탕 n 킬로그램 배달
    // 3kg, 5kg 봉지 있음
    // 설탕 n 킬로를 정확하게 배달할 때 몇 봉지 필요한지?

    // 먼저 큰 수인 5로 나누어보고, 나누어 떨어지는게 3이 되는지 보자.

    int N;
    cin >> N;

    int count = 100000;

    // 5로 먼저 나눠보자
    int div = N / 5;

    for (int i = 0; i <= div; i++) {
        int rest = N - (5 * i);
        int cnt = i;

        if (rest % 3 == 0) {
            cnt += rest / 3;
            rest = 0;
        }
        if (0 < cnt < count && rest == 0) {
            count = cnt;
        }
    }

    if (count == 100000) {
        cout << -1;
    } else {
        cout << count;
    }

}