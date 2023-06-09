/*
https://www.acmicpc.net/problem/8980<br/>
택배<br/>
8980
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
using namespace std;

int main() 
{
    int N, C , M; // N 은 마을 수 | C 는 트럭 용량 | M 은 택배 정보 갯수
    cin >> N >> C >> M;

    vector<vector<int>> boxes(M, vector<int>(3));

    int start, end , num;
    for (int i = 0; i < M ; i++){
        cin >> start >> end >> num;
        boxes[i][0] = start;
        boxes[i][1] = end;
        boxes[i][2] = num;
    }
    sort(boxes.begin(), boxes.end());
    int stop = N;
    int sol = 0;
    int wei = 0;
    for (int i = 0; i < N ; i++){
        for (int j = 0; j < M ; j++){
            if(boxes[j][1]== i){
                sol +=
            }
        }
    }

    cout << sol << endl;
}

   /*  for (int i = 0; i < N-1 ; i++){
        cout <<  sol << endl;
        for (int j = i+1; j <N ; j++){
            if(boxes[i][j] != 0){
                if()
                stop = min(stop,j);
                sol += boxes[i][j];
            }
        }
        if(stop != N){
            i = stop;
            stop = N;
        }
    } */