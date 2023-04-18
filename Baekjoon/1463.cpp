#include <iostream>
#include <algorithm>

using namespace std;

int dp[1000001];

int main(){

    int N;
    cin >> N;
    
    for(int i = N-1; i > 0; i--){
        if(i > N/2){
            dp[i] = dp[i+1]+1;
        }
        else if(i > N/3){
            dp[i] = min(dp[i+1]+1, dp[2*i]+1);
        }
        else{
            dp[i] = min(min(dp[i+1]+1, dp[2*i]+1), dp[3*i]+1);
        }
    }
    cout << dp[1] << '\n';

    return 0;
}