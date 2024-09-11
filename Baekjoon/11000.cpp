#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    if (a.first < b.first) {
        return true;
    }
    return false;
}

int main() {
    
    // Si -> Ti 끝나는 N개의 수업
    // 최소의 강의실을 사용해서 모든 수업을 가능하게!
    // 수업이 끝난 직후에 다음 수업을 시작할 수 있다. 즉 <= 인경우에 같이 들을 수 있음

    int n;
    cin >> n;
    
    vector<pair<int, int> > v;
    priority_queue<int, vector<int>, greater<int> > t;

    for (int i = 0; i < n; i++) {
        int s, t;
        cin >> s >> t;
        v.push_back(make_pair(s, t));
    }

    // 일단 어떤 수업의 시작시간과 어떤 수업의 끝나는 시간이 겹치는 구간이 있으면 같이 들을 수 없음
    // 즉 겹치는 구간 발생시 강의실이 하나가 추가가 됨

    // 일단 시작하는 시간 순으로 정렬해볼까?

    // 아니엇음. 끝나는 시간을 우선으로 생각하여 접근해야 됨!
    // 우선순위 큐를 쓰라는데?

    sort(v.begin(), v.end(), compare);

    for (int i = 0; i < n; i++) {
        t.push(v[i].second);
        if (t.top() <= v[i].first) {
            t.pop();
        }
    }
    cout << t.size();
}