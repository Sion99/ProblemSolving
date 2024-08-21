#include <iostream>
#include <string>

using namespace std;

int main() {
    // 바킹독 문자열

    // 특정 패턴과 일치하는 파일 이름 출력 못함
    // 패턴은 소문자 여러개와 * 하나로 이루어진 문자열

    // 파일 이름이 패턴에 일치하려면, 패턴에 있는 별표를 임의의 문자열로 변환
    // abcd, ad, anestonestod ->  a*d 로 변경가능
    
    // 별표 기준으로 남아있는 값들만 직접 비교하면 될듯!

    int n;
    string pattern;
    cin >> n;
    cin >> pattern;

    int k = 0;
    while (pattern[k] != '*') {
        k++;
    }

    string front = pattern.substr(0, k);
    string back = pattern.substr(k + 1);

    for (int i = 0; i < n; i++) {
        string file;
        cin >> file;

        // 여기서 조건문 체크를 잘 해줘야 런타임에러(out of bounds)가 안뜸
        if (file.size() >= front.size() + back.size()) {
            if (front.compare(file.substr(0, k)) == 0) {
                if (back.compare(file.substr(file.size() - back.size())) == 0) {
                    cout << "DA" << '\n';
                }
                else {
                    cout << "NE" << '\n';
                }
            }
            else {
                cout << "NE" << '\n';
            }
        } else {
            cout << "NE" << '\n';
        }
    }
}