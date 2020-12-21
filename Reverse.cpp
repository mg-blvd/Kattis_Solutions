//
//  Reverse.cpp
//  Kattis_Tester
//
//  Created by Misael Guijarro on 12/20/20.
// Partially Accepted

#include <string>
#include <iostream>
using namespace std;

int main() {
    string inputNum;
    string output = "";
    int amount;

    cin >> amount;
    for(int i = 0; i < amount; i++) {
        cin >> inputNum;
        output = inputNum + "\n" + output;
    }

    cout << output;

}
