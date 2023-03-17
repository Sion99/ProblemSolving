#include <iostream>

using namespace std;

typedef struct member
{
    string name;
    int age;
    int weight;
} member;

int main()
{
    member m;
    while (1)
    {
        cin >> m.name >> m.age >> m.weight;
        if (m.name == "#")
            break;
        if (m.age > 17 || m.weight >= 80)
            cout << m.name << " Senior\n";
        else
            cout << m.name << " Junior\n";
    }
}