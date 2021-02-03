//#include <bits/stdc++.h>
//
//using namespace std;
//
//int main() {
//    int n, m, k;
//    vector<int> v;
//    cin >> n >> m >> k;
//    for (int i = 0; i < n; i++) {
//        int x;
//        cin >> x;
//        v.push_back(x);
//    }
//
//    sort(v.begin(), v.end());
//
//    int first = v[n - 1];
//    int second = v[n - 2];
//
//    int count = m / (k + 1) * k + m % (k + 1);
//    int result = first * count;
//    result += second * (m - count);
//    cout << result << endl;
//}