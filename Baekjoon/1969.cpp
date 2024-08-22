#include <iostream>
#include <string>
#include <vector>

using namespace std;

char findMax(int a, int t, int g, int c) {
    if (a >= c && a >= g && a >= t) {
        return 'A';
    }
    if (c > a && c >= g && c >= t) {
        return 'C';
    }
    if (g > a && g > c && g >= t) {
        return 'G';
    }
    return 'T';
}

int hamming_distance(string a, string b) {
    int dist = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            dist++;
        }
    }
    return dist;
}

int main() {
    // DNA 뉴클오티드 문자
    // Hamming Distance 계산하기
    // AGCAT, GGAAT 두 글자 다르므로 hd = 2

    int n, m;
    cin >> n >> m;

    vector<string> dnas;
    for (int i = 0; i < n; i++) {
        string dna;
        cin >> dna;
        dnas.push_back(dna);
    }

    // 결국에는 모든 DNA와 최대한 많이 겹치는 DNA S를 찾아야 함
    // 살짝 그리디하게 접근하면 될듯?
    // 모든 문자열에서 가장 많이 나오는 값을 고르면 될 거 같은데

    string s = "";

    for (int i = 0; i < m; i++) {
        int a = 0;
        int t = 0;
        int g = 0;
        int c = 0;
        for (int j = 0; j < n; j++) {
            switch (dnas[j][i]) {
                case 'A':
                    a++;
                    break;
                case 'T':
                    t++;
                    break;
                case 'G':
                    g++;
                    break;
                case 'C':
                    c++;
                    break;
            }
        }
        s += findMax(a, t, g, c);
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += hamming_distance(dnas[i], s);
    }
    cout << s << '\n';
    cout << sum << '\n';
}