/*
https://www.acmicpc.net/problem/2156
포도주 시식
2156
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> grape(n+1);

    for(int i = 1 ; i <= n ; i++){
        cin >> grape[i];
    }
    
    vector<int> dp(n+1);
    dp[0] = 0;
    for(int i = 1 ; i <= n; i += 3){
        dp[i] = max(max(dp[i-1],dp[i-1]+ grape[i]),grape[i]);
    }
    cout << dp[n] << endl;
}