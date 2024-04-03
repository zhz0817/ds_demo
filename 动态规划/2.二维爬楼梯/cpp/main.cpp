#include "bits/stdc++.h"
using namespace std;
//https://leetcode.cn/problems/unique-paths/
class Solution {
public:
    int uniquePaths(int m, int n) {
        int dp[m+1][n+1];
        for(int i=1;i<=m;i++){
            dp[i][1] = 1;
        }
        for(int i=1;i<=n;i++){
            dp[1][i] = 1;
        }
        for(int i=2;i<=m;i++){
            for(int j=2;j<=n;j++){
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m][n];
    }
};
int main(){
    Solution s;
    return 0;
}