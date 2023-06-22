/*
https://www.acmicpc.net/problem/19700<br/>
수업<br/>
19700
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <queue>
using namespace std;

int main() 
{
    int N,x,y;
    cin >> N;
    priority_queue<pair<int,int>> pq;
    for (int i = 0; i < N ; i++){
        cin >> x >> y;
        pq.push(pair<int,int>(x,y));
    }
    int sol = 0;
    vector<int> team;
    while(!pq.empty()){
        /* cout << pq.top().first <<" "<<pq.top().second <<endl;
        pq.pop(); */
        int len = pq.top().first;
        int lev = pq.top().second;

        if(lev == 1){
            team.push_back(1);
        }
    }
}