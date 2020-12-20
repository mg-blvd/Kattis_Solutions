#include <iostream>
#include <algorithm>
using namespace std;

int findCorrectDifference(int numbers[]){
  int d1 = numbers[1] - numbers[0];
  int d2 = numbers[2] - numbers[1];
  if(d1 > d2)
    return d2;
  return d1;
}

int newNum(int numbers[], int diff){
  if(numbers[1] - numbers[0] == numbers[2] - numbers[1])
    return numbers[2] + diff;
  else if(numbers[1] - numbers[0] == diff)
    return numbers[1] + diff;
  else
    return numbers[0] + diff;
}

int main(){
int nums[4], difference, missing;
  for(unsigned i = 0; i < 3; i++)
    cin >> nums[i];
  sort(nums, nums + 3);
  difference = findCorrectDifference(nums);
  missing = newNum(nums, difference);
  cout << missing;
  return 0;
}
