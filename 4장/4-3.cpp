#include <bits/stdc++.h>
using namespace std;

string input;
int row;
int col;

int dx[8] = {-2,-2,-1,-1,1,1,2,2};
int dy[8] = {-1,1,-2,2,-2,2,-1,1};

int main() {
    int count = 0;
    cin>>input;
    row = int(input[1]) - 48;
    col = int(input[0]) - 96;

    for(int i = 0;i<8; i++) {
        int nextX = row + dx[i];
        int nextY = col + dy[i];
        if (nextX >=1 && nextX <= 8 && nextY>=1 && nextY <= 8) {
            count++;
        }
    }

    cout<<count<<endl;

}