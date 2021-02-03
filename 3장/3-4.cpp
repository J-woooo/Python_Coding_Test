#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    int count = 0;

    cin >> n >> k;
    // 23 3
    while (true)
    {
        int target = (n / k) * k;
        count += (n - target);
        // n이 k보다 작을 때 반복문 탈출
        n = target;
        if (n < k)
            break;
        n /= k;
        count += 1;
    }
    count += (n - 1);
    cout << count << endl;
}