/* 
231. Power of Two
Given an integer, write a function to determine if it is a power of two.
*/
#include<stdbool.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
bool isPowerOfTwo(int n){
    if(n<=0)
        return false;
    else{
        return ( ((~n+1) & n) == n);
    }
}

void main(int argc , char* argv[]){
    int x =  atoi(argv[1]);
    isPowerOfTwo(x) ? printf("yes\n"):printf("false\n");
}