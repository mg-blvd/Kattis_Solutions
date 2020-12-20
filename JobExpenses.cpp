#include <iostream>
using namespace std;

int main(){
  unsigned sets, total = 0;
  int curNum;
  cin >> sets;
  for(unsigned i = 0; i < sets; i++)
  {
    cin >> curNum;
    if(curNum < 0)
    {
      total += -curNum;
    }
  }
  cout << total;
  return 0;
}
