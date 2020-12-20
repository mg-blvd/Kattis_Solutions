#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  string morse_symbols[2][30] = {{}, {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "..--", ".-.-", "---.", "----"}};
  string message, new_message, char_lengths, new_chars[4] = {"_", ",", ".", "?"};
  int index;
  for(int i = 0; i < 26; i++)
    morse_symbols[0][i] = string(1, static_cast<char>(i + 65));
  for(int i = 0; i < 4; i++)
    morse_symbols[0][i + 26] = new_chars[i];

  while(cin >> message)
  {
    new_message = "";
    char_lengths = "";
    for(int i = 0; i < message.length(); i++)
    {
      for(int y = 0; y < 30; y++)
      {
        if(morse_symbols[0][y] == string(1, message[i]))
        {
          index = y;
          break;
        }
      }
      new_message.append(morse_symbols[1][index]);
      char_lengths.append(string(1, static_cast<char>(morse_symbols[1][index].length() + 48)));
      reverse(char_lengths.begin(), char_lengths.end());
    }
    cout << new_message << " " << char_lengths << endl;
  }
  return 0;
}
