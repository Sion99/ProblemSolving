#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

vector<string> split(string s) {
    vector<string> v;
    size_t start = 0;
    size_t end = s.find(' ');
    while (end != string::npos) {
        v.push_back(s.substr(start, end - start));
        start = end + 1;
        end = s.find(' ', start);
    }
    v.push_back(s.substr(start, end - start));
    return v;
}

int main() {
    
    int t;
    cin >> t;
    cin.ignore();

    for (int i = 0; i < t; i++) {
        string voices;
        getline(cin, voices);

        vector<string> v = split(voices);

        // 여우 울음소리
        map<string, string> m;
        string audio;
        while (true) {
            getline(cin, audio);
            if (audio.compare("what does the fox say?") == 0) {
                break;
            }
            vector<string> v2 = split(audio);
            m[v2[0]] = v2[2];
        }
        for (int i = 0; i < v.size(); i++) {
            int flag = 0;
            for (auto x : m) {
                if (x.second.compare(v[i]) == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                cout << v[i] << ' ';
            }
        }
    }
}