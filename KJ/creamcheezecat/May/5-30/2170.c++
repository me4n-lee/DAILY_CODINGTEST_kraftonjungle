/*
https://www.acmicpc.net/problem/2170<br/>
선 긋기<br/>
2170
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
    int N ;
    cin >> N;
    map<long long,long long> pot;
    map<long long,long long>::iterator i;
    int x , y;
    for (int i = 0; i < N; i++){
        cin >> x>>y;
        pot[x] = y; 
    }
    long long sol = 0;

    /*  for(i = pot.begin(); i != pot.end() ; i++){
        cout << i->first << " : "<< i->second << endl;
    } */
    long long start = pot.begin()->first;
    long long end = pot.begin()->second;
    for(i = pot.begin(); i != pot.end() ; i++){
        if(end < i->first){
            sol += end - start;
            start = i->first;
            end = i->second;
        }else{
            end = max(end, i->second);
        }

    }
    sol += end - start; 
    cout << sol << endl;
}