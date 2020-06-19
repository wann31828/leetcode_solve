#include<stdio.h>
#include<stdbool.h>
#include<math.h>

bool isprime(int n){
    for(int i =2 ; i*i <n ;i++){
        if ( (n%i) ==0)
            return false ;
    }
    return true ;
}

bool isprime_fast(int n){
	    if (n == 2 || n == 3) {
	        return true;
	    } else if (n > 4) {
	        int m = n % 6;
	 
	        if (m != 1 && m != 5) {
	            return false;
	        }
	 
	        int nSqrt = (int)sqrt((double)n);
	 
	        for (int i = 5; i <= nSqrt; i += 6) {
	            if (n % i == 0 || n % (i + 2) == 0) { // n % i: 6n + 5 -> 6(n + 1) - 1 -> 6n - 1, n % (i + 2): 6n + 1
	                return false;
	            }
	        }
	 
	        return true;
	    } else {
	        return false;
	    }
}
/*
204
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

 */
int count_prime(int n){
    int count = 0;
    if(n <2)
        return 0;
    else if(n==2)
        return 1;

    for(int i=3;i<n; i+=2){
        if(isprime_fast(i))
            count++;
    }

    return count+1 ;
}
