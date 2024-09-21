#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

int main() {

    // D 킬로미터 길이 고속도로
    // 지름길 존재, 일방통행
    int arr[10002] = {0, };
    int n, d;
    cin >> n >> d;

    vector<tuple<int, int, int> > shortcut;

    // 지름길 전부 입력받고
    // 일단, 지름길 끝이 d보다 크거나, 지름길이 지름길이 아닌 경우 제외
    for (int i = 0; i < n; i++) {
        int st, end, len;
        cin >> st >> end >> len;

        if ((len > end - st) || (end > d)) {
            continue;
        }
        shortcut.push_back(make_tuple(st, end, len));
    }

    for (int i = 0; i < 10002; i++) {
        arr[i] = i;
    }

    // 다이내믹 프로그래밍으로 풀어보기
    // 전체 총 길이는 10000을 넘지 않음
    // 10000짜리 배열을 선언하고, 처음부터 시작해서, 지름길 있으면 지름길로 가고, 없으면 1 추가

    // for (int i = 0; i <= d; i++) {
    //     for (int j = 0; j < shortcut.size(); j++) {
    //         if (get<0>(shortcut[j]) == i) {
    //             int next = get<1>(shortcut[j]);
    //             int len = get<2>(shortcut[j]);
    //             arr[next] = min(arr[next], arr[i] + len);
    //         }
    //     }
    //     // 만약에 현 위치에 shortcut이 없다면?
    //     arr[i + 1] = arr[i] + 1;
    // }

    for (int i = 1; i <= d; i++) {
        arr[i] = arr[i - 1] + 1;
        for (int j = 0; j < shortcut.size(); j++) {
            if (get<1>(shortcut[j]) == i) {
                int before = get<0>(shortcut[j]);
            }
            if(get<0>(shortcut[j]) == i)
            {
                int next = get<1>(shortcut[j]);
                int len = get<2>(shortcut[j]);
                arr[next] = min(arr[next - 1] + 1, arr[i] + len);
            }
        }
    }

    cout << arr[d] << '\n';

}