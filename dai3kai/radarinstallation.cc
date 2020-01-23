#include <utility> // pair のため
#include <algorithm> // sort のため
#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int k = 0;
    while(1){
        k++;
        //input
        int n, d;
        int flag = 0; //cheak y>d
        pair <int,int> IS[1010];
        for (int i=0; i<1010;i++) IS[i] = make_pair(0, 0); //init IS
        cin >> n >> d;
        if (n==0 && d==0) break;
        for (int i=0;i<n;i++) {
            int x,y;
            cin >> x >> y;
            if (y > d) flag = 1;
            IS[i] = make_pair(x + sqrt(d^2 - y^2),x - sqrt(d^2 - y^2));
        }
        //solution
        int r = 0;
        if (flag == 0) {
            sort(IS, IS+n);
            int memory = -2147483648;
            int c = 0;
            for (int i=0; i<n;i++){
                if (memory < IS[i].second){
                    r += 1;
                    memory = IS[i].first;
                }
            }
        }

        //output
        if (flag == 1){
            cout << "Case " << k << ": "<<-1 << endl;
        }
        else {
            cout << "Case " << k << ": "<< r << endl;
        }

    }
}

