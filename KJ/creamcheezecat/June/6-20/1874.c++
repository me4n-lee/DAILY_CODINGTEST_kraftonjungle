/*
https://www.acmicpc.net/problem/1874<br/>
스택 수열<br/>
1874
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <stack>
using namespace std;

int main() 
{
    int N, now,target = 1;
    cin >> N;
    stack<int> s;
    stack<int> sol;
    for(int i = N; i > 0  ; i--){
        s.push(i);
    }
    sol.push(s.top());
    s.pop();
    for(int i = 0; i < N ; i++){
        cin >> now;
        if(sol.top() < now){
            while(sol.top() <= now){
                sol.push(s.top());
                cout << "+" << endl;
                s.pop();
            }
            cout << "-" <<endl;
            sol.pop();
        }else if(sol.top() == now){
            cout << "-" <<endl;
            sol.pop();
        }else{
            cout << "NO" << endl;
            break;
        }
    }
}