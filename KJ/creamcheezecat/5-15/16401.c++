/* 
https://www.acmicpc.net/problem/16401
과자 나눠주기
16401 
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int main() {
    int M,N;
    cin >> M >> N;

    vector<unsigned long long> snack(N);

    for(int i = 0 ; i < N ; i++){
        cin >> snack[i];
    }
    sort(snack.begin(),snack.end());

    int left = 0, right = snack[N-1];
    
    while(left <= right){
        int mid = (left + right) / 2;

        for (int i = 0 ; i < N; i++){
            
        }
    }

    /* 
    if(M <= N){
        cout << snack[N-M]<< endl;
    }else{
        for(int j = 0; j < snack.size()-1 ; j++){
            if( snack[j] < snack[N]/(M-(N-1))){
                cout << snack[N] << endl;
                return 0;
            }
        }
        cout << snack[N]/(M-(N-1)) << endl;
        
    } */
}
