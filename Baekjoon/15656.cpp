#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int arr[10];
int num[10];

void func(int k) {
    // k == m에 도달할 경우 다 출력하고 끝
    if (k == m) {
        for (int i = 0; i < m; i++) {
            cout << num[arr[i]] << ' ';
        }
        cout << '\n';
        return;
    }
    // 아직 채워야 할 공간이 있다면
    for (int i = 0; i < n; i++) {
        arr[k] = i;
        func(k + 1);
    }

    // 0 -> 0 0 -> 0 0 0
    // 0 -> 0 1 -> 0 0
}

int main() {

    cin >> n >> m;
    // 같은 수 여러번 골라도 됨

    for (int i = 0; i < n; i++) {
        cin >> num[i];
    }
    sort(num, num + n);
    func(0);
}