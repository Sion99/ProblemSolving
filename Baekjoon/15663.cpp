#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int arr[10];
int num[10];
bool isused[10];

// 일단 중복 수열 빼고는 다 해결했는데.. 중복을 어떻게 해결하지?


void func(int k) {
    if (k == m) {
        for (int i = 0; i < m; i++) {
            cout << num[arr[i]] << ' ';
        }
        cout << '\n';
        return;
    }
    // 아직 채울 곳이 남았다면
    int last_used = -1;
    for (int i = 0; i < n; i++) {
        if (!isused[i] && num[i] != last_used) {
            arr[k] = i;
            isused[i] = 1;
            func(k + 1);
            isused[i] = 0;
            last_used = num[i];
        }
    }
}

int main() {
    // 중복 수열 안됨
    // 사전 순 증가 순서 출력
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> num[i];
    }
    
    sort(num, num + n);
    func(0);

}