//
//  ShatteredCake.cpp
//  Kattis_Tester
//
//  Created by Misael Guijarro on 12/21/20.
//

#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int width, pieceWidth, pieceLength, numPieces, area = 0;
    cin >> width;
    cin >> numPieces;
    
    for(int i = 0; i < numPieces; i++) {
        cin >> pieceWidth >> pieceLength;
        area += pieceLength * pieceWidth;
    }
    
    cout << area / width;
    return EXIT_SUCCESS;
}
