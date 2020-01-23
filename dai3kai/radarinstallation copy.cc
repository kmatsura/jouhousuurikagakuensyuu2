#include <utility> // pair のため
#include <algorithm> // sort のため
#include <iostream>
using namespace std;

int main() {
    while(1){
        //input
        int n, d;
        int flag = 0; //cheak y>d
        pair <int,int> IS[1010];
        cin >> n >> d;
        if (n==0 && d==0) break;
        for (int i=0;i<n;i++) {
            int x,y;
            cin >> x >> y;
            if (y > d) flag = 1;
            IS[i] = make_pair(x, y);
        }
        //solution
        if (flag == 0) {
            
        }

        //output
        if (flag == 1){
            cout << -1 << endl;
        }
        else {

        }

    }
}

