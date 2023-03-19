#include <iostream>

using namespace std;

int main()
{
    int num, temp;
    int count = 0;
    cin >> num;
    for (int i = 0; i < 5; i++)
    {
        cin >> temp;
        if (temp % 10 == num)
            count++;
    }
    cout << count;
}