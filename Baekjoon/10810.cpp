#include <iostream>

using namespace std;

int main() {
    int N, M, a, b, c;

    cin >> N >> M;

    int arr[101];

    for (int i = 0; i < 101; i++) {
        arr[i] = 0;
    }

    for (int i = 0; i < M; i++) {
        // a번부터 b번까지 c번 번호가 적혀져 있는 공
        cin >> a >> b >> c;
        for (int j = a; j <= b; j++) {
            arr[j] = c;
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << ' ';
    }
}