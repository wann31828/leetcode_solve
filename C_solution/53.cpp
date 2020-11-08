#include<vector>
#include <algorithm>
#include<limits>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int localmax = 0, globalmax = INT_MIN;
        for (int n:nums){
            localmax = max(localmax+n,n);
            globalmax = max(localmax,globalmax);
        }
        return globalmax;
    }
};