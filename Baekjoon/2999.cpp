#include <iostream>
#include <string>
#include <math.h>

using namespace std;

char matrix[101][101];

int main() {
    // 메시지 총 N 글자
    // R <= C, R*C = N 인 R, C 고름
    // 여러 개일 경우, R 큰값 선택
    // R * C 행렬 생성

    // 메시지를 행렬에 옮기고 (-> 방향),
    // 읽을때는 아래로 읽는다

    string message;
    cin >> message;

    int n = int(message.size());
    int c = 1;
    int r = 1;
    int s = (double)sqrt(n);

    for (int i = 1; i <= s; i++) {
        if (n % i == 0) {
            r = i;
        }
    }
    c = n / r;

    int cnt = 0;
    
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            matrix[j][i] = message[cnt++];
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << matrix[i][j];
        }
    }
}