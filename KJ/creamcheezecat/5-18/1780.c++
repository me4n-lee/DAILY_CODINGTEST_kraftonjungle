/*
https://www.acmicpc.net/problem/1780
종이의 개수
1780
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

void dfs(vector<vector<int>> arr,int n , int &o , int &z, int &m){
    bool flag = false;
    int first_num = arr[0][0];

    for (int j = 0; j < n ; j++){
        for (int i = 0; i< n ; i++){
            if (first_num != arr[j][i]){
                flag = true;
                break;
            }
        }
        if (flag){
            break;
        }
    }


    if(!flag){
        switch (first_num)
        {
        case 1:
            o++;
            break;
        case 0:
            z++;
            break;
        case -1:
            m++
            break;
        }

        return ;
    }else{
        if (n > 1) {
            int section = n/3;
            for (int k = 0 ; k< 9 ; k++){
                vector<vector<int>> subpaper(section ,vector<int>(section) );
                for(int j = 0; j < section ; j++){
                    for(int i = 0; i< section ; i++){
                        subpaper[j*section][i*section];
                    }
                }
                dfs(subpaper,section,o,z,m)
            }
            
        }else{
            printf("오류 ?? 여기오면 안되는데??")
        }

    }

}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> paper(N, vector<int>(N));

    int one = 0, zero = 0, mone = 0;

    for(int j = 0; j < N ; j++){
        for(int i = 0; i< N ; i++){
            cin >> paper[j][i];
        }
    }

    dfs(paper, N , one , zero, mone);

    cout << mone << '\n'<< zero << '\n' << one <<endl;


    // cout <<  endl;
    // for(int j = 0; j < N ; j++){
    //     for(int i = 0; i< N ; i++){
    //         cout << paper[j][i] << " ";
    //     }
    //     cout << endl;
    // }
    return 0;
}