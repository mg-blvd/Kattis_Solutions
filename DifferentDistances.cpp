//Not DoneS
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
  double x1, y1, x2, y2, p, result;
  cin >> x1;
  while(x1 != 0){
    cin >> y1;
    cin >> x2;
    cin >> y2;
    cin >> p;
    x1 = pow(abs(x1 - x2), p);
    x2 = pow(abs(y1 - y2), p);
    result = pow(x1 + x2, 1/p);
    cout << fixed;
    cout << setprecision(10) << result << endl;
    cin >> x1;
  }
  return 0;
}
