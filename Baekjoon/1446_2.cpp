#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
    int n, d;
    cin >> n >> d;

    vector<int> arr(10001, 10001);
    vector<pair<int, int> > v[10001];
    for (int i = 0; i < n; i++) {
        int st, end, len;
        cin >> st >> end >> len;

        if (st > end || len > end - st) {
            continue;
        }

        v[end].push_back(make_pair(st, len));
    }

    arr[0] = 0;

    for (int i = 1; i <= d; i++) {
        arr[i] = arr[i - 1] + 1;
        for (int j = 0; j < int(v[i].size()); j++) {
            arr[i] = min(arr[i], arr[v[i][j].first] + v[i][j].second);
        }
    }

    cout << arr[d];
}