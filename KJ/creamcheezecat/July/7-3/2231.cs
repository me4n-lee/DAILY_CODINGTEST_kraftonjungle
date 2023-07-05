/*
https://www.acmicpc.net/problem/2231<br/>
분해합<br/>
2231
*/

using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;

namespace BaekJoon
{
    static class Program{
        static void Main(){
            int input = int.Parse(Console.ReadLine());

            int Sum = 0;     //각 자리수의 합
            int result = 0;  //abc+a+b+c

            for(int i=0;i<input;i++)
            {
                char[] ChArray=i.ToString().ToCharArray();

                for(int j=0;j<ChArray.Length;j++)
                {
                    Sum+=int.Parse(ChArray[j].ToString());                
                }
                result = Sum + i;
            
                if(result==input)
                {
                    Console.WriteLine(i);
                    break;
                }  
                else if(i==input-1&&result!=input)
                {
                    Console.WriteLine(0);
                }
                Sum = 0;
            }
        }
    }
}