#include <bits/stdc++.h>
using namespace std;

int n, m, x, y, direction;
// 방문한 위치를 저장하기 위한 맵
int d[50][50];
int arr[50][50];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void turn_left() {
    direction -= 1;
    if (direction == -1) direction = 3;
}

int main() {
    cin>>n>>m;
    cin>>x>>y>>direction;
    d[x][y] = 1;
    for(int i = 0;i<n;i++) {
        for(int j = 0;j<m;j++) {
            int x;
            cin>>x;
            arr[i][j] = x;
        }
    }

    // 시뮬레이션 시작
    int cnt = 1;
    int turn_time = 0;
    while(1) {
        turn_left();
        int nx = x + dx[direction];
        int ny = y + dy[direction];
        // 회전한 이후 정면에 가보지 않은 칸이 존재하지 않은 경우 이동
        if (d[nx][ny] == 0 && arr[nx][ny] == 0) {
            d[nx][ny] = 1;
            x = nx;
            y = ny;
            cnt += 1;
            turn_time = 0;
            continue;
        }
        // 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else {
            turn_time += 1;
        }
        if (turn_time == 4) {
            nx = x - dx[direction];
            ny = y - dy[direction];
            // 뒤로 갈 수 있다면 이동하기
            if (arr[nx][ny] == 0) {
                x = nx;
                y = ny;
            }
            // 위가 바다로 막혀있는 경우
            else break;
            turn_time = 0;
        }
    }
    cout<<cnt<<endl;
}