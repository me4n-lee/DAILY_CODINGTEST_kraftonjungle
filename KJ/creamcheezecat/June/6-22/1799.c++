/*
https://www.acmicpc.net/problem/1799<br/>
비숍<br/>
1799
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
using namespace std;

void 

int main() 
{
    int N;
    cin >> N;
    vector<vector<int>> ch(N,vector<int>(N,0));
    vector<vector<bool>> vi(N,vector<int>(N,false));
    for (int i = 0; i < N ; i++){
        for(int j = 0; j < N ; j++){
            cin >> ch[i][j];
            if(ch[i][j] == 0){
                vi[i][j] = true;
            }
        }
    }

    

/*     for (int i = 0; i < N ; i++){
        for(int j = 0; j < N ; j++){
            cout << ch[i][j] << " ";
        }
        cout << endl;
    } */
}