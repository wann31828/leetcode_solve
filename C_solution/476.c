/* 
476. Number Complement
Easy

Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


*/
#include<stdio.h>
int main(){
    int x = 1 ,count = 0 ,y = 0;
    int tmp = x ,rt = 0;
    while(tmp){
        tmp =  tmp>> 1;
        count ++;
    }
    while(count){
        y |= 1;
        count --;
        if(count)
            y = y<<1;
    }
    rt = ~x & y ;
    printf("com of %d is %d\n",x,rt) ;
}

int findComplement(int num){
    int tmp = num ,count = 0 , y = 0;
        while(tmp){
        tmp =  tmp>> 1;
        count ++;
    }
    while(count){
        y |= 1;
        count --;
        if(count)
            y = y<<1;
    }
    return (~num & y);
}