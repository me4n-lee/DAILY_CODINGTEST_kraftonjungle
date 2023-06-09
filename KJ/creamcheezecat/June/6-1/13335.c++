/*
https://www.acmicpc.net/problem/13335<br/>
트럭<br/>
13335
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
    int  n, w, L; // n 다시를 건너는 트럭의수, w는 다리의 길이 , L 다리의 하중
    cin >> n >> w >> L ;

    vector<int> truck(n,0);
    for (int i = 0; i < n; i++){
        cin >> truck[i];
    }

    vector<int> bridge(w,0);

    int times = 0;
    int weight = 0;
    int num = 0;

    while(!bridge.empty()){
        time++;
        
        
    }
    /* for (int i = 0; i < n-1 ; i++){
        while(true){
            if(truck[i] + truch[i+1] > L){
                time += w;
                break;
            }else{
                times++;
            }
            
        }
    } */

    cout << times << endl;
}