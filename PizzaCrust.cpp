//Not Done
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
  int crust, radius;
  double pizza_area, cheese_area;
  cin >> radius;
  cin >> crust;
  pizza_area = pow(radius, 2) * 3.14;
  cheese_area = pow((radius - crust), 2) * 3.14;
  cout << fixed;
  cout << setprecision(9) << 100 * cheese_area / pizza_area;

  return 0;
}
