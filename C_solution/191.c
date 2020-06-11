#include <stdlib.h>
#include <stdint.h>

/*
191. Number of 1 Bits
Write a function that takes an unsigned integer
and return the number of '1' bits it has

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string
00000000000000000000000000001011 has a total of three '1' bits.

 */
int hammingWeight(uint32_t n) {
    int count = 0;
    while(n){
        count++;
        n &= (n-1);
    }
    return count;
}