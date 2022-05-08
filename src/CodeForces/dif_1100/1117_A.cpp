#include<iostream>
using namespace std;


int main() { 
    int n; cin >> n;
    int max = 0;
    int len = 0;
    int max_len = 0;

    for (int i; i<n; i++){
        int a; cin >> a;

        if (a > max){
            max = a;
        }

        if (a == max){
            len += 1;
        }
        else{
            if (len > max_len){
                max_len = len;
            }
            len = 0;
        }
    }
    cout << max_len << endl;
	return 0;
}