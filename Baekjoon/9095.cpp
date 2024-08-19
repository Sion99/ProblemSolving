#include <iostream>

using namespace std;

int main() {
    // 1, 2, 3의 합으로 n을 나타내기
    // 나타낼 수 있는 총 방법의 수

    int t;
    cin >> t;
    int arr[100001] = {0, };

    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;

    for (int i = 4; i < 11; i++) {
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
    }

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        cout << arr[n] << '\n';
    }
}