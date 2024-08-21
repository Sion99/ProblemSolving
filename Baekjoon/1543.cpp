#include <iostream>
#include <string>

using namespace std;

int main() {

    // 영어로만 이루어진 문서 검색
    // 어떤 단어 총 몇번 등장하는지?
    // 단 중복은 빼고
    // 동시에 셀 수는 없음, 즉 한 번 세면 그 문자 이후에 다시 셀 수 있다.

    // 입력 값에 "a a a a a" 처럼 공백이 포함된 문자열이 올 수도 있는데,
    // 이를 위해 getline으로 입력을 받는다.

    string doc, query;
    getline(cin, doc);
    getline(cin, query);

    int query_size = int(query.size());

    int count = 0;

    for (int i = 0; i < doc.size(); i++) {
        string sub = doc.substr(i, query_size);
        if (sub.compare(query) == 0) {
            count++;
            i += (query_size - 1);
        }
    }
    cout << count << '\n';
}