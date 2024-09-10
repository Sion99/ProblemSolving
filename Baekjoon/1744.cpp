#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> minus_nums;
    vector<int> plus_nums;
    int zero_cnt = 0;
    int one_cnt = 0;

    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;

        if (num < 0)
            minus_nums.push_back(num);
        else if (num == 0)
            zero_cnt++;
        else if (num == 1)
            one_cnt++;
        else
            plus_nums.push_back(num);
    }

    sort(minus_nums.begin(), minus_nums.end());               // 음수는 오름차순으로 정렬
    sort(plus_nums.begin(), plus_nums.end(), greater<int>()); // 양수는 내림차순으로 정렬

    int sum = 0;

    // 양수 처리
    for (int i = 0; i + 1 < plus_nums.size(); i += 2)
    {
        sum += plus_nums[i] * plus_nums[i + 1];
    }
    if (plus_nums.size() % 2 == 1)
    {
        sum += plus_nums.back(); // 홀수개일 경우 마지막 남은 하나 더해줌
    }

    // 음수 처리
    for (int i = 0; i + 1 < minus_nums.size(); i += 2)
    {
        sum += minus_nums[i] * minus_nums[i + 1];
    }
    if (minus_nums.size() % 2 == 1 && zero_cnt == 0)
    {
        sum += minus_nums.back(); // 홀수개 남았는데 0이 없으면 더해줌
    }

    // 1은 곱하는 것보다 더하는 게 유리하므로 그냥 더함
    sum += one_cnt;

    cout << sum << '\n';

    return 0;
}
