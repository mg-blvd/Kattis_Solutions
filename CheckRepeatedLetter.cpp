#include <iostream>
#include <string>
using namespace std;

bool hasDuplicate(string word){
  for(unsigned i = 0; i < word.length() - 1; i++)
  {
    int curr_position;
    curr_position = word.find(word[i], i + 1);
    if(curr_position != -1)
      return true;
  }
  return false;
}

int main(){
  string word;
  cin >> word;
  cout << hasDuplicate(word);
  return 0;
}
