#include <vector>
#include <string>

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        vector<vector<int>> dp(s.length(), vector<int>(s.length(), 0));

        // Init
        for(int i=0; i<s.length(); i++)
            dp[i][i] = 1;

        // Build DP table
        for(int start = s.length()-1; start>=0; start--) {
            for(int end = start+1; end<s.length(); end++) {
                if(s[start] == s[end])
                    dp[start][end] = 2 + dp[start+1][end-1];
                else
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1]);
            }
        }

        return dp[0][s.length()-1];
    }
};