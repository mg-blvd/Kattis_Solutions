#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
  int setCount;
  int total = 0, numCount, * numbers;
  double classAver;
  int countAboveAver;
  double percAboveAver;
  cin >> setCount;
  for(unsigned i = 0; i < setCount; i++)
  {
    total = 0;
    countAboveAver = 0;
    cin >> numCount;
    numbers = new int[numCount];
    for(unsigned y = 0;y < numCount; y++)
    {
      cin >> numbers[y];
      total += numbers[y];
    }
    classAver = total / numCount;
    for(unsigned y = 0; y < numCount; y++)
    {
      if(numbers[i] > classAver)
        countAboveAver++;
    }
    percAboveAver = countAboveAver / numCount;
    cout << fixed;
    cout << setprecision(3) << percAboveAver * 100 << "%\n";
    delete[] numbers;
  }
  return 0;
}
