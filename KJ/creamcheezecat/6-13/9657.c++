/*
https://www.acmicpc.net/problem/9657<br/>
돌 게임3<br/>
9657
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
using namespace std;


int main() 
{// 상근이 먼저 시작  상근이 이기면 SK  창영이 이기면 CY
    int N;
    cin >> N;
    // 1,3,4 상근 = 0 창영 = 1
    // 
    vector<int> dp(N+1,0);
    
    dp[0] = 0;
    for(int i = 1; i <= N; i++){
         dp[i] = 1; // 상근이의 패배로 초기화

        if (i >= 1 && dp[i - 1] == 0)
            dp[i] = 0;
        if (i >= 3 && dp[i - 3] == 0)
            dp[i] = 0;
        if (i >= 4 && dp[i - 4] == 0)
            dp[i] = 0;
    }
    
    if (dp[N] == 0)
        cout << "SK" << endl;
    else
        cout << "CY" << endl;

    return 0;
    
}