#include <iostream>

using namespace std;

int main() {
    // 1. 3으로 나누어 떨어지면 3으로 나눈다
    // 2. 2로 나누어 떨어지면 2로 나눈다
    // 3. 1을 뺀다

    int n;
    cin >> n;
    int cnt = 0;

    int arr[1000001] = {0, };

    int i = 0;

    for (int i = 2; i <= n; i++) {
        arr[i] = arr[i - 1] + 1;
        if (i % 2 == 0) {
            arr[i] = min(arr[i], arr[i / 2] + 1);
        }
        if (i % 3 == 0) {
            arr[i] = min(arr[i], arr[i / 3] + 1);
        }
    }
    cout << arr[n];
}