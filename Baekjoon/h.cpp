#include <iostream>

using namespace std;

int ask(int x) {
    cout << "? " << x;
    cout.flush();
    int num;
    cin >> num;
    return num;
}

void answer(int n, int m) {
    cout << "! " << n << ' ' << m;
    cout.flush();
}

int main() {
    
    // 10^9이 이하의 음이 아닌 정수 N과 양의 정수 M 예측하기!

    // 10^9 이하 양의 정수 X -> X 배수와 N과의 차이 중에서 가장 작은 값을 M으로 나눈 나머지
    // 질문은 최대 100번

    // 각 줄 출력 후 표준 출력 버퍼 비워줘야 함
    
    int x = 2;
    int n = 0;
    int m = 1;

    while (1) {
        // x의 배수와 N과의 차이 중에서 가장 작은 값을 M으로 나눈 나머지
        int diff_x = ask(x);

        

    }
}