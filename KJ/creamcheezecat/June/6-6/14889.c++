/*
https://www.acmicpc.net/problem/14889<br/>
스타트와 링크<br/>
14889
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <stdlib.h>
using namespace std;

int sol = 10000;

void dfs(vector<vector<int>>& sta, vector<int>& team,int n, int idx, int cnt ){
    if(cnt == n/2){
        int diff;
        for(int i = 0 ; i < n/2; i++){
            for (int j = i; j < n/2 ; j++){
                diff += status[i]                
            }
        }
    }
}

int main() 
{
    int N;
    cin >> N;

    vector<vector<int>> status(N,vector<int>(N,0));
    vector<int> team(N,0);
    for (int i = 0; i < N ; i++){
        for (int j = 0; j < N; j++){
            cin >> status[i][j];
        }
    }

    /* int sol=10000;
    for(int i = 0 ; i < N; i++){
        for (int j = i; j < i+(N/2) ; j++){

        }
    } */
    
}