#include <iostream>
#include <string>

using namespace std;

int count_colons(string ipv4) {
    int cnt = 7;
    for (int i = 0; i < ipv4.size(); i++) {
        if (ipv4[i] == ':') {
            cnt--;
        }
    }
    return cnt;
}

int main() {
    // IPv6는 길이가 128비트인 차세대 프로토콜
    // 32자리의 16진수를 4자리씩 :으로 끊어 나타냄
    // 2001:0db8:85a3:0000:0000:8a2e:0370:7334

    // 1. 각 그룹의 앞자리의 0의 전체 또는 일부 축약 가능
    // 2001:db8:0:00:8a2e:370:7334

    // 2. 만약 0으로만 이루어져 있는 그룹이 있을 경우 한 개 이상 연속된 그룹을 골라 :: 로 바꿀 수 있음
    // 2001:db8:85a3::8a2e:370:7334

    // 2번 규칙은 딱 한 번만 사용할 수 있음
    // 축약형 IPv6 주소를 원래 IPv6 주소로 복원하기

    string ipv4;
    cin >> ipv4;

    int remains = count_colons(ipv4);

    for (int i = 0; i < ipv4.size(); i++) {
        
    }
    
    
}