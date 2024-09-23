#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {

    // 배낭 문제
    // 배낭에 최대 가치를 가지고 갈 수 있도록
    // n개의 물건, 무게 w, 가치 v
    // 최대 k만큼의 무게제한
    int n, k;
    cin >> n >> k;

    int arr[100001] = {0};
    vector<int> > v[100001];
    
    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;

        v[w].push_back(v);
    }

    for (int i = 0; i < k; i++) {
        arr[i] = min(arr[i], arr[i] + v[arr[i]]);
    }

    


}