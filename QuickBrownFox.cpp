#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main()
{
  string message;
  bool lettersFound[26];
  for(unsigned i = 0; i < 26; i++)
    lettersFound[i] = false;
  getline(cin, message);
  for(unsigned i = 0; i < message.length(); i++)
  {
    if(isalpha(message[i]))
    {
      lettersFound[tolower(message[i]) - 97] = true;
    }
  }
  if(find(lettersFound, false) == -1)
    cout << "pangram";
  else
  {
    cout << "missing ";
    for(unsigned i = 0; i < 26; i++)
    {
      if(lettersFound[i] == false)
        cout << static_cast<char>(i + 96);
    }
  }
  return 0;
}
