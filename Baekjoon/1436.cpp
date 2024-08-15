#include <iostream>
#include <string>

using namespace std;

int check(int num) {
    string str = to_string(num);

    auto idx = str.find("666");

    if (str.find("666") == string::npos) {
        return 0;
    } else {
        return 1;
    }
}

int main() {
    // 종말의 수 666
    // N 번째 영화의 제목에 들어가는 수
    // 적어도 3개 이상 6이 연속으로
    int n;
    cin >> n;

    int count = 0;
    int num = 665;
    while (1) {
       int result = check(++num);
       if (result == 1) {
            count++;
       }
       if (count == n) {
            break;
       }
    }
    cout << num;
}