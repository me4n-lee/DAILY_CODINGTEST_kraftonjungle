/*
https://www.acmicpc.net/problem/5430<br/>
AC<br/>
5430
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <sstream>
using namespace std;

int main() 
{
    int T;
    cin >> T;
    while(T--){
        string comm;
        cin >> comm;
        int n;
        cin >> n;
        string numb;
        vector<int> numbers;
        cin >> numb;

        // 문자열에서 숫자와 쉼표를 제외한 모든 문자를 공백으로 치환
        for (char& c : numb){
            if (c == '[' || c == ']' || c == ',')
                c = ' ';
        }

        std::stringstream ss(numb);
        int num;
        // 문자열에서 숫자 추출 
        while (ss >> num)
        {
            numbers.push_back(num);
        }

        // 함수 연산
        for (string::iterator iter = comm.begin(); iter != comm.end(); ++iter)
        {
            if(*iter == 'R'){
                reverse(numbers.begin(),numbers.end());
            }else{
                if(numbers.size() == 0){
                    break;
                }
                numbers.erase(numbers.begin());
                
            }
            
        }
        vector<int>::iterator it;
        if(numbers.size() == 0){
            cout << "error" <<endl;
        }else{
            cout <<"[";
            for(it = numbers.begin(); it != numbers.end() ; it++){
                cout << *it << ",";
            }
            cout << "]" <<endl;
        }

            
    }
}