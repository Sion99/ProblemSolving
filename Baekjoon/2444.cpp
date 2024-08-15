#include <iostream>

using namespace std;

int main() {
    // 첫째 줄 부터 2*N - 1번째까지 별 출력
    // 1 -> 1줄
    // 2 -> 3줄
    // 3 -> 5줄
    // 4 -> 7줄...
    // 5 -> 9줄
    // 1 3 5 7 9 7 5 3 1

    int N;
    cin >> N;

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < N - i; j++) {
            cout << ' ';
        }

        for (int j = 0; j < 2*i - 1; j++) {
            cout << "*";
        }
        cout << '\n';
    }
    for (int i = N; i >= 1; i--) {
        for (int j = N - i; j > 0; j--) {
            cout << ' ';
        }

        for (int j = 2*i - 1; j > 0; j--) {
            cout << "*";
        }
        cout << '\n';

    }
    
}