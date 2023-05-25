/*
https://www.acmicpc.net/problem/2302<br/>
극장 좌석<br/>
2302
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
    int N, M;
    cin >> N >> M;

    map<int,bool> chaircase(N+1,false);
    
    int x;
    for (int i = 0; i < M ; i++){
        cin >> x;
        chaircase[x] = true;
    }

    // dp 로직을 아예 생각이 안남


}