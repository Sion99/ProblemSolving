#include <iostream>

using namespace std;

int main()
{
    int n, m;
    int ans;

    cin >> n >> m;
    ans = comb(n, m);
    cout << ans << endl;
}