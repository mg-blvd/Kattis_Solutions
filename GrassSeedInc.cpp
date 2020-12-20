#include <iostream>
#include <iomanip>
using namespace std;

int main(){
  double price, length, width, total = 0, sqr_meters;
  unsigned sets;
  cin >> price;
  cin >> sets;
  for(int i = 0; i < sets; i++)
  {
    cin >> width;
    cin >> length;
    sqr_meters = width * length;
    total += price * sqr_meters;
  }
  cout << fixed;
  cout << setprecision(7) << total;
  return 0;
}
