/*
386. Lexicographical Numbers
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

 */
#include <iostream> 
#include <string>
#include <vector> 
#include <algorithm>
using namespace std; 

class Solution {
    vector<string> nums;
    vector<int> rtnums;
public:
    vector<int> lexicalOrder(int n) {
        for(int x =1;x<=n ;x++)
            nums.push_back(to_string(x));
        sort(nums.begin(), nums.end());

        for(auto x: nums)
            rtnums.push_back(stoi(x));
        
        return rtnums;
    }
};

int main() { 

    vector<string> nums;
    for(int x =1;x<=15 ;x++)
        nums.push_back(to_string(x));
    sort(nums.begin(), nums.end());

    for(auto ch : nums) {
        cout << ch << endl;
    }

    return 0; 
}