#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int result = -1;
	for (int i = 0; i < m; i++) {
		int min_value = 10001;
		for (int j = 0; j < n; j++) {
			int x;
			cin >> x;
			min_value = min(x, min_value);
		}
		result = max(result, min_value);
	}
	cout << result << endl;
}