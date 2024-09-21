#include <iostream>
#include <vector>

using namespace std;

// 소수 판별기
bool isprime(int num) {
    if (num < 2) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int next_nonprime(int num) {
    while (1) {
        ++num;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return num;
            }
        }
    }
}

int main() {
    
    // 소수가 아닌 양의 정수 N개를 골라 공차가 M인 등차수열 만들기
    // 등차수열 찾기

    int n, m;
    cin >> n >> m;

    // 범위는 2 000 000 이하
    
    // 첫항 a는 1로 주자
    // 등차수열 항 -> a + (n - 1)d
    
    int i = 1;
    int cnt = 0;
    vector<int> v;

    while (cnt < n) {
        cnt++;
        int next = i + (cnt - 1) * m;
        if (next <= 2000000 && !isprime(next)) {
            v.push_back(next);
        } else {
            i = next_nonprime(i);
            cnt = 0;
            v.clear();
        }
    }

    if (cnt == n) {
        for (int i = 0; i < v.size(); i++) {
            cout << v[i] << ' ';
        }
    }
    else {
        cout << -1;
    }
}