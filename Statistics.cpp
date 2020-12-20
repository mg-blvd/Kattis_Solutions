//Not Done

#include <iostream>
#include <algorithm>
#include <array>
using namespace std;

int main(){
  int arr_size, counter = 1, minimum, maximum, *arr;
  while(cin >> arr_size){
    arr = new int[arr_size];
  for(unsigned i = 0; i < arr_size; i++)
    cin >> arr[i];
  minimum = min(*arr);
  cout << "Case " << counter << ": " << result.first << " " << result.second << " "
   << result.second - result.first << endl;
   delete[] arr;
   counter++;
  }
  return 0;
}
