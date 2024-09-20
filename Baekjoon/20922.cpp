#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 수열에서 같은 원소 여러 개 들어 있는 수열 X
    // 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이 구하기

    int n, k;
    cin >> n >> k;

    vector<int> v;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }

    // 투 포인터?
    // 같은 정수가 k개 이하이면 돼
    
    int front = 0;
    int back = 0;
    int arr[200001] = {0, };
    int max_len = 0;
    int length = 0;

    while (back < n) {
        // 만약 front == back 인 경우
        // 길이가 0이고, back을 한 칸 앞으로 보낸다
        // 길이 1 증가
        
        // 만약 front < back이고
        // 아직 k를 초과하지 않았다면
        // back을 다시 한 칸 더 밀어 보낸다
        // 길이 1 증가

        // 만약 front < back 이고
        // k를 초과했다면
        // back은 멈추고
        // front를 한 칸 밀어 초과하지 않도록 한다
        // 길이는 1 감소

        // 만약 다시 front == back이 되면
        // 길이가 0이고, back을 한 칸 앞으로 보낸다

        if (arr[v[back]] != k)
        {
            arr[v[back]]++;
            back++;
        }
        else
        {
            arr[v[front]]--;
            front++;
        }
        max_len = max(max_len, back - front);
    }
    cout << max_len;
}