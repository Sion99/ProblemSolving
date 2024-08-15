#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    // 도화지는 가로세로 각각 100
    // 색종이 가로세로 각각 10

    int arr[101][101];

    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            arr[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;

        for (int i = a; i < a + 10; i++) {
            for (int j = b; j < b + 10; j++) {
                arr[i][j] = 1;
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < 101; i++)
    {
        for (int j = 0; j < 101; j++)
        {
            if (arr[i][j] == 1) {
                cnt++;
            }
        }
    }
    cout << cnt;
}