#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b) {
	return a > b;
}

int main() {

	// 로프를 병렬로 연결하면 로프에 걸리는 중량 나눌 수 있음
	// k개 로프 사용하여 w 무게 들어올릴 때, 각각에 고르게 w/k 만큼 중량
	// 로프들을 이용해 들어올릴 수 있는 물체 최대 중량
	// 일단 전체로 따지면, 로프 최솟값 중량까지 최대로 올릴 수 있다
	// 임의의 몇 개만 골라도 되기 때문에 하나씩 적은 로프 하나씩 쳐 내면서 비교해봐야할듯?

	int N;
	cin >> N;

	vector<int> v;

	for (int i = 0; i < N; i++) {
		int w;
		cin >> w;

		v.push_back(w);
	}

	sort(v.begin(), v.end(), compare);

	int max = v[v.size() - 1] * v.size();
	
	for (int i = 1; i < N - 1; i++) {
		v.pop_back();

		int curr_weight = v[v.size() - 1] * v.size();

		if (curr_weight > max) {
			max = curr_weight;
		}
	}

	cout << max;
}