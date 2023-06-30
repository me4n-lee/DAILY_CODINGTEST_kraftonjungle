/*
https://www.acmicpc.net/problem/11728
배열 합치기
11728
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
using namespace std;

int main() 
{
    int a,b,n,temp = 0;
    cin >> a >> b;
    vector<int> A;

    for(int i = 0; i < a ; i++){
        cin >> n;
        A.push_back(n);
    }

    for (int i = 0; i < b ; i++){
        cin >> n;
        while(true){
            if(A[temp] > n){
                A.insert(A.begin() + temp,n);
                break;
            }
            temp++;
        }
    }

    for (int i = 0; i < a + b; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}