#include <iostream>
#include <string>

using namespace std;

int main() {
    // 길이가 N인 문자열 하나 주어졌을 때 gori에서 주어진 문자열에서 유래되었는지?
    // gori를 연속 부분 문자열로 가지는지?

    int n;
    cin >> n;

    string s;
    cin >> s;

    int i = 0;
    while (s[i]) {
        string temp = s.substr(i, 4);
        if (temp.compare("gori") == 0) {
            cout << "YES";
            return 0;
        }
        i++;
    }
    cout << "NO";
}