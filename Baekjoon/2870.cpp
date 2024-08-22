#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b) {
    if (a.size() == b.size()) {
        return a < b;
    } else {
        return a.size() < b.size();
    }
}

int main() {

    // 알파벳 소문자로 되어있는 글자 N줄
    // 숫자 모두 찾고, 비내림차순 정렬
    // 숫자의 앞에 0이 있는 경우 생략 가능

    // 숫자가 나오는 경우 가능한 가장 큰 숫자 찾아야 함
    // 01a2b3456cde478 -> 1, 2, 3456, 478

    // 숫자 다 찾고, 오름차순 정렬하기

    // 문제는, 최대 100글자가 들어올 수 있기 때문에 숫자로 변환이 불가능함
    // 오직 문자열로만 취급해서 비교 및 저장을 해야하는 구조
    
    int n;
    cin >> n;

    vector<string> numbers; 

    for (int i = 0; i < n; i++) {
        string content;
        cin >> content;

        int j = 0;
        int last = 0;
        while (content[j]) {
            if (content[j] >= '0' && content[j] <= '9') {
                last = j++;
                while (content[j] >= '0' && content[j] <= '9') {
                    j++;
                }
                string sub = content.substr(last, j - last);
                int k = 0;
                while (sub[k] == '0') {
                    k++;
                }
                sub = sub.substr(k);
                if (sub == "") {
                    sub = "0";
                }
                numbers.push_back(sub);
            } else {
                j++;
            }
        }
    }

    sort(numbers.begin(), numbers.end(), compare);
    for (int i = 0; i < numbers.size(); i++) {
        cout << numbers[i] << '\n';
    }
}