#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool hasUpper(string variable) {
    int i = 0;
    while (variable[i]) {
        if (variable[i] >= 'A' && variable[i] <= 'Z') {
            return true;
        }
        i++;
    }
    return false;
}

bool hasUnderbar(string variable) {
    int i = 0;
    while (variable[i]) {
        if (variable[i] == '_') {
            return true;
        }
        i++;
    }
    return false;
}

bool checkValid(string variable) {
    int i = 0;
    if (variable[0] == '_') {
        return false;
    }
    if (variable[0] >= 'A' && variable[0] <= 'Z') {
        return false;
    }
    while (variable[i]) {
        if (variable[i] == '_') {
            if (variable[i + 1] == '_') {
                return false;
            }
        }
        i++;
    }
    if (variable[i - 1] == '_') {
        return false;
    }
    return true;
}

vector<string> split_java(string variable) {
    vector<string> words;

    int i = 0;
    int last = 0;
    while (variable[i] >= 'a' && variable[i] <= 'z') {
        i++;
    }
    
    // 제일 처음 시작한 단어는 소문자로 시작하니까 바로 삽입
    string sub = variable.substr(last, i - last);
    words.push_back(sub);

    // 이제부터 단어는 대문자로 시작
    while (variable[i]) {
        if (variable[i] >= 'A' && variable[i] <= 'Z') {
            // 대문자의 경우 길이 세기
            last = i++;
            while (variable[i] >= 'a' && variable[i] <= 'z') {
                i++;
            }
            sub = variable.substr(last, i - last);
            words.push_back(sub);
        } else {
            i++;
        }
    }
    return words;
}

vector<string> split_cpp(string variable) {
    vector<string> words;

    int i = 0;
    int last = 0;

    while (variable[i] >= 'a' && variable[i] <= 'z') {
        i++;
    }

    // 제일 처음 시작한 단어는 소문자로 시작하니까 바로 삽입
    string sub = variable.substr(last, i - last);
    words.push_back(sub);

    while (variable[i]) {
        if (variable[i] == '_') {
            last = ++i;
            while (variable[i] >= 'a' && variable[i] <= 'z') {
                i++;
            }
            sub = variable.substr(last, i - last);
            words.push_back(sub);
        } else {
            i++;
        }
    }
    return words;
}

int main() {
    // Java는 첫 단어 소문자, 나머지 단어는 첫 문자만 대문자
    // 모든 단어는 붙여쓴다
    // c++은 소문자만, 단어 사이에는 _

    // c++ 형식은 Java 형식으로, Java 형식은 c++로

    // 변수명 입력으로 받아서 어떤 언어 형식인지 파악할 것
    // 다음으로 반대 형식으로 변환할 것

    string variable;
    cin >> variable;

    // 일단 글자에 대문자 또는 _ 가 있는지 체크
    // 둘 다 있으면 error

    if (!checkValid(variable)) {
        cout << "Error!\n";
        return 0;
    }

    if (hasUpper(variable) && hasUnderbar(variable)) {
        cout << "Error!\n";
        return 0;
    }

    if (hasUpper(variable)) {
        // Java 확률이 높음
        vector<string> words = split_java(variable);
        for (int i = 0; i < words.size(); i++) {
            // 소문자로 만들고, 글자 사이에 _ 추가
            for (int j = 0; j < words[i].size(); j++) {
                if (words[i][j] >= 'A' && words[i][j] <= 'Z') {
                    words[i][j] += 32;
                }
            }
            cout << words[i];
            if (i < words.size() - 1) {
                cout << '_';
            }
        }
        return 0;
    }

    if (hasUnderbar(variable)) {
        // c++ 확률이 높음
        vector<string> words = split_cpp(variable);
        for (int i = 0; i < words.size(); i++) {
            // 앞글자 대문자로 만들기
            if (i > 0) {
                words[i][0] -= 32;
            }
            cout << words[i];
        }
        return 0;
    }

    // 대문자도 없고, 언더바도 없다면 한 단어일 것임. 따라서 변환 없이 출력해주면 됨.
    cout << variable << '\n';


}