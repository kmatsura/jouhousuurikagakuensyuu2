#include <utility> // pair のため
#include <algorithm> // sort のため
#include <iostream>
using namespace std;

int T, N, K, X[100000+10], A[100000+10];
int main() {
    cin >> T; // データセットの数を読み込む
    for (int t=0; t<T; ++t) {
        // 家と発電機の数を読み込む
         cin >> N >> K;
        for (int i=0; i<N; ++i) cin >> X[i]; // 家の位置を入力
        for (int i=0; i<100010;i++) A[i]=0; //init A
        for (int i=1; i<N; ++i) A[i-1] = X[i]-X[i-1]; // 家と家の間
        // 配列 A を整列する
        sort(A ,A+N-1);
        // 配列 A の先頭 max(0,N-1-(K-1)) 個の和を出力する
        int ans = 0;
        int temp = N - K;
        if (temp > 1) {
            for (int i=0; i<temp; ++i){
                ans += A[i];
            }
        }
        else if (temp == 1) {            
        ans = A[0];    
        }
        
        else {
            ans = 0;
        }
        cout << ans << endl;
    }
}
