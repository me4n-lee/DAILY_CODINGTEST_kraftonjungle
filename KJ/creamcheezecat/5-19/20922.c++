/*
https://www.acmicpc.net/problem/20922
겹치는 건 싫어
20922
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    vector<int> proc(N);
    vector<int> checking(200001, 0);
    for (int i = 0 ; i < N ; i++ ){
        cin >> proc[i];
    }

    int longcount = 0;
    int curcount = 0;
    for (int i = 0 ; i < N ; i++){
        checking[proc[i]] += 1;
        if(checking[proc[i]] > K){
            checking[proc[i]] = 1;
            curcount = 1;
        }else{
            curcount += 1;
            longcount = max(longcount,curcount);
        }
    }

    cout << longcount <<endl;

}