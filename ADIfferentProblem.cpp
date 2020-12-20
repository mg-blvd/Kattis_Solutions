#include <cmath>
#include <iostream>
using namespace std;

int main()
{
   long long first_num, second_num;
  while(cin >> first_num)
  {
    cin >> second_num;
    cout << abs(first_num - second_num) << endl;
  }
  return 0;
}
