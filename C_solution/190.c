#include <stdint.h>
#include <stdio.h>
/*

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
 so return 964176192 which its binary representation is 00111001011110000010100101000000.

 */
uint32_t reverseBits(uint32_t n) {
    printf("input: %u\n",n);
    uint32_t tar =0; 
    for(int i = 0; i<32 ;i++){
        printf("tar:%u , n:%u \n",tar,n);
        tar |= ((n & 0x1) << (31-i)) ;
        n = n >>1 ;
    }
    printf("res: %u\n",tar);
    return tar ;
}

void main(void){
    uint32_t x = 4294967293;
    reverseBits(x);
}