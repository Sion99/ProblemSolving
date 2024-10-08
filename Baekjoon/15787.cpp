#include <iostream>

using namespace std;

int main() {
    // n개의 기차
    // 기차에는 20개의 일렬로 된 좌석
    // 1~n번 기차가 있을 때 M개의 명령
    
    // 1 i x: i번째 기차에 x번째 좌석에 사람 태우기
    // 2 i x: i번째 기차에 x번째 좌석에 사람 하차
    // 3 i: i번째 기차에 앉아있는 승객들 모두 한 칸씩 뒤로, 20번째인 경우는 하차
    // 4 i: i번째 기차에 앉아있는 승객들 모두 한 칸씩 앞으로, 1번째인 경우는 하차

    // 회전하는 큐와 비슷한 문제인듯?

    // M번의 명령 후에 1번째 기차부터 순서대로 한 기차씩 은하수를 건너는데 조건이 있음
    // 기차내 좌석 상태가 중복이 되면 안됨 -> 즉, 이것을 집합으로 해서 중복을 제거해야 할 듯?
    
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int order_num, train_num, x_num;
        cin >> order_num >> train_num >> x_num;

        cout << order_num << ' ' << train_num << ' ' << x_num << '\n';
    }
}