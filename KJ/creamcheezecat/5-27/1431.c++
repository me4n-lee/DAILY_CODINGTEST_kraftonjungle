/*
https://www.acmicpc.net/problem/1431<br/>
시리얼 번호<br/>
1431
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
    vector<string> serial(N);
    for (int i = 0 ; i < N ; i++){
        cin >> serial[i];

    }
    for (int k = 0 ; k < N*(N-1) ; k++)
    {
        for (int i = 0 ; i < N-1 ; i++){
            if(serial[i].length() > serial[i+1].length()){
                swap(serial[i],serial[i+1]);
            }else if (serial[i].length() == serial[i+1].length()){
                int sercount = 0;
                int lsum=0,rsum=0;
                while(sercount <= serial[i].length()){
                    if(isdigit(serial[i].at(sercount))){
                        lsum += serial[i].at(sercount) - '0';
                    }

                    if(isdigit(serial[i+1].at(sercount))){
                        rsum += serial[i+1].at(sercount) - '0';
                    }

                    sercount++;
                }
                
                if(lsum > rsum){
                    swap(serial[i],serial[i+1]);
                }
            }
        }

    }

    for (int i = 0 ; i < N ; i++){
        cout << serial[i] << endl;
    }
}