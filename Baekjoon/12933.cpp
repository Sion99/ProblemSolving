#include <iostream>
#include <string>
#include <vector>

using namespace std;

int find_alphabet(char c, vector<string> v) {
    for (int i = 0; i < v.size(); i++) {
        if (v[i][v[i].size() - 1] == c) {
            return i;
        }
    }
    return -1;
}

int main() {
    // 오리 울음소리 "quack"
    // 올바른 오리 울음소리 -> 울음소리 한 번 또는 그 이상 연속해서

    // 울음 소리가 섞이는데, 방에 있을 수 있는 오리의 최소 수

    string quack;
    cin >> quack;

    int i = 0;

    // 울음소리는 무조건 q -> u -> a -> c -> k로 가야함
    // 스택을 여러 개 둘까?
    // 문자열 벡터를 여러개 둬서 쭉 가는 것도 괜찮을듯


    // 해결 방법: q가 들어오면 k로 끝나는 칸이 있으면 이어서 진행, 없으면 새롭게 추가
    vector<string> v;
    int idx;
    while (quack[i]) {
        switch (quack[i]) {
            case 'q':
                idx = find_alphabet('k', v);
                if (idx == -1) {
                    v.push_back("q");
                } else {
                    v[idx] += 'q';
                }
                break;
            case 'u':
                idx = find_alphabet('q', v);
                if (idx == -1) {
                    cout << -1 << '\n';
                    return 0;
                } else {
                    v[idx] += 'u';
                }
                break;
            case 'a':
                idx = find_alphabet('u', v);
                if (idx == -1) {
                    cout << -1 << '\n';
                    return 0;
                }
                else {
                    v[idx] += 'a';
                }
                break;
            case 'c':
                idx = find_alphabet('a', v);
                if (idx == -1) {
                    cout << -1 << '\n';
                    return 0;
                } else {
                    v[idx] += 'c';
                }
                break;
            case 'k':
                idx = find_alphabet('c', v);
                if (idx == -1) {
                    cout << -1 << '\n';
                    return 0;
                } else {
                    v[idx] += 'k';
                }
                break;
        }
        i++;
    }
    for (int i = 0; i < v.size(); i++) {
        if (v[i].size() % 5 != 0) {
            cout << -1 << '\n';
            return 0;
        }
    }
    cout << int(v.size()) << '\n';

    
}