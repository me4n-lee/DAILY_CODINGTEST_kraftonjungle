/*
https://www.acmicpc.net/problem/14501<br/>
퇴사<br/>
14501
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
    int N;
    cin >> N;

    map<int,int> days;
    map<int,int> profit;

    map<int,int> dp;
    int maxprofit = 0;
    int daycount;
    for (int i = 0; i < N ; i++){
        cin >> days[i] >> profit[i];
    }

    for (int i = 0; i < N ; i++){
        daycount = 0;
        while(daycount <= N){
            dp[i] += profit[daycount];
            daycount += days[i+daycount];
        }
        maxprofit = max(maxprofit,dp[i]);
    }

    cout << maxprofit << endl;

}