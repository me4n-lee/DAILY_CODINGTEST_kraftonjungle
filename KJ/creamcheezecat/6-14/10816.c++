/*
https://www.acmicpc.net/problem/10816<br/>
숫자 카드<br/>
10816
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
    
    long long N, M;
    cin >> N;
    vector<long long> handcard(N);
    for (int i = 0; i < N ; i++){
        cin >> handcard[i];
    }
    cin >> M;
    vector<long long> numcard(M);
    for (int i = 0; i < M ; i++){
        cin >> numcard[i];
    }

    sort(handcard.begin(),handcard.end());

    int sol;
    long long left,right,mid;
    for (int i = 0; i < M ; i++){
        sol = 0;
        left = 0;
        right = N-1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (handcard[mid] == numcard[i]) {
                sol++;
                int j = mid - 1;
                while (j >= 0 && handcard[j] == numcard[i]) {
                    sol++;
                    j--;
                }
                j = mid + 1;
                while (j < N && handcard[j] == numcard[i]) {
                    sol++;
                    j++;
                }
                break;
            } else if (handcard[mid] < numcard[i]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        cout << sol << ' ';
    }

    cout << endl;
}