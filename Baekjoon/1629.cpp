#include <iostream>

using namespace std;

int main()
{
    long long a, b, c;
    long long answer;

    cin >> a >> b >> c;
    answer = 1;
    while (b > 0)
    {
        if (b % 2 == 1)
            answer = (answer * a) % c;
        a = ((a % c) * (a % c)) % c;
        b /= 2;
    }
    cout << answer << endl;
}