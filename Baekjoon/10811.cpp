#include <iostream>

using namespace std;

int main() {
    // 바구니 N개
    // 1 ~ N
    // M번 바구니 순서 역순

    int N, M, a, b;
    int arr[101];

    for (int i = 0; i < 101; i++) {
        arr[i] = i;
    }

    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        cin >> a >> b;

        for (int j = 0; j <= (b-a) / 2; j++) {
            int temp = arr[a + j];
            arr[a + j] = arr[b - j];
            arr[b - j] = temp;
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << ' ';
    }
}