/*
https://www.acmicpc.net/problem/1202<br/>
보석 도둑<br/>
1202
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
using namespace std;

struct Jewel{
    long long m; // 무게
    long long v; // 가격
};

bool compareJewel(const Jewel& jewel1, const Jewel& jewel2) {
    return jewel1.m < jewel2.m;
}



int main() 
{
    long long N , K ; // N 보석 총 갯수, K 가방 총 갯수 , C 는 가방의 최대 무게
    cin >> N >> K;
    
    vector<Jewel> jewel(N);
    vector<long long> backpack(K);
    long long x,y;

    for (long long i = 0; i < N ; i++){
        cin >>x >> y;
        jewel[i].m = x;
        jewel[i].v = y;
    }

    for (long long i = 0; i < K ; i++){
        cin >>backpack[i];
    }

    long long sol = 0;

    sort(jewel.begin(),jewel.end(),compareJewel);
    sort(backpack.begin(),backpack.end());


    for(long long i = 0; i < N ; i++){
        if(backpack.size()==0){
                break;
        }
        for (long long j = 0 ; j <backpack.size() ; j++){
            if(jewel[i].m <= backpack[j]){
                sol += jewel[i].v;
                backpack.erase(backpack.begin(),backpack.begin()+j+1);
                break;
            }
        }
    }

    cout << sol << endl;
}