#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;

    cin >> n;
    vector<int> arr(n);
    vector<int> arr2(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    copy(arr.begin(), arr.end(), arr2.begin());
    sort(arr.begin(), arr.end());
    
}