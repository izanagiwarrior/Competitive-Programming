#include <iostream>
using namespace std;
int main() {
    int Jumlah; cin >> Jumlah;
    int ArrayX[Jumlah],ArrayY[Jumlah],ArrayZ[Jumlah];
    for (int i = 0; i < Jumlah; i++) {
        cin >> ArrayX[i] >> ArrayY[i] >> ArrayZ[i];
    }
    for (int i = 0; i < Jumlah; i++){
        for (int j = 0; j < ArrayZ[i]; j++){
            if(ArrayX[i] > ArrayY[i]){
                ArrayX[i] = ArrayX[i] / 2;
            }
            else if(ArrayX[i] < ArrayY[i]){
                ArrayY[i] = ArrayY[i] / 2;
            }
            else if(ArrayX[i] == ArrayY[i] && ArrayX[i] > 0){
                ArrayX[i] = ArrayX[i] / 2;
            }
            else if(ArrayX[i] == 0 && ArrayY[i] == 0){
                break;
            }
            else if(ArrayX[i] == 1 ){
                ArrayX[i] = 0;
            }
            else if(ArrayY[i] == 1){
                ArrayY[i] = 0;
            }
        }
    if(ArrayX[i] > ArrayY[i]){
        cout << ArrayX[i] << " " << ArrayY[i] << "\n";
    }
    else if(ArrayX[i] < ArrayY[i]){
        cout << ArrayY[i] << " " << ArrayX[i] << "\n";
    }
    else if(ArrayX[i] == ArrayY[i]){
        cout << ArrayX[i] << " " << ArrayX[i] << "\n";
    }
    }
}