#include <iostream>
#include <queue>
#include <utility>
#include <map>

// 주의해야할 것
// 1. 배열을 쓰면 메모리 초과가 일어남
// 2. int형을 쓰면 오버플로우가 일어남

using namespace std;

int main()
{
    long long a, b;
    cin >> a >> b;
    queue<pair<long long, long long>> Q;
    map<long long, long long> map;
    map.insert({a, 0});
    Q.push({a, 0});
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        if (cur.first == b)
        {
            cout << cur.second + 1 << '\n';
            return 0;
        }
        long long arr[2] = {2 * cur.first, (10 * cur.first) + 1};
        for (int i = 0; i < 2; i++)
        {
            if (arr[i] > b)
                continue;
            auto item = map.find(arr[i]);
            if (item != map.end())
                continue;
            Q.push({arr[i], cur.second + 1});
            map.insert({arr[i], cur.second + 1});
        }
    }
    cout << "-1\n";
}