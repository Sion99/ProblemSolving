#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // 이름 궁합이란 두 사람의 이름을 한 글자씩 번갈아 써 놓고,
    // 획수를 그 아래에 적은 뒤, 인접한 숫자끼리 더한 일의 자리 값을 계속 적어나감

    // 알파벳 대문자 이름 궁합
    // 알파벳 대문자 획수는 주어짐
    int arr[26] = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};
    string A;
    string B;

    // 두 문자열 A, B의 길이는 같음
    cin >> A >> B;

    vector<int> result;

    for (int i = 0; i < A.size(); i++) {
        result.push_back(arr[A[i] - 'A']);
        result.push_back(arr[B[i] - 'A']);
    }

    while (result.size() > 2) {
        for (int i = 0; i < result.size() - 1; i++) {
            result[i] = (result[i] + result[i + 1]) % 10;
        }
        result.pop_back();
    }
    cout << result[0] << result[1];
}