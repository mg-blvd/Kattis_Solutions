#include <iostream>
using namespace std;

int main()
{
  int amountOfSets, amountOfGnomes, starter, current;
  cin >> amountOfSets;
  for(int i = 0; i < amountOfSets; i++)
  {
    cin >> amountOfGnomes;
    cin >> starter;
    for(int y = 2; y <= amountOfGnomes; y++)
    {
      cin >> current;
      if(current != starter + 1)
        cout << y << endl;
      else
        starter = current;
    }
  }
  return 0;
}
