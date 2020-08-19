#include <string>
#include "memory.h"
/*
dp[i, j]   = 1                                               if i == j

           = s[i] == s[j]                                if j = i + 1

           = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1  
 */
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) 
            return "";
        int n = s.size(), dp[n][n] , left = 0, len = 1;
        memset(dp,0,n*n*sizeof(int));

        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
            for (int j = 0; j < i; ++j) {
                dp[j][i] = (s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]));
                if (dp[j][i] && len < i - j + 1) {
                    len = i - j + 1;
                    left = j;
                }
            }
        }
        return s.substr(left, len);
    }
};