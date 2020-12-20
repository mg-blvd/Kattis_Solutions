#include <string>
#include <iostream>
using namespace std;

int getVal(char cur){
  switch(cur){
    case ' ':
      return 0;
    case '\'':
    case '`':
      return 3;
    case '.':
      return 4;
    case '"':
      return 6;
    case ',':
    case '-':
    case '^':
      return 7;
    case ':':
    case '_':
      return 8;
    case '!':
    case '~':
      return 9;
    case '/':
    case '<':
    case '>':
    case '\\':
      return 10;
    case ';':
      return 11;
    case '(':
    case ')':
    case '|':
      return 12;
    case '+':
    case 'r':
    case 'x':
    case 'v':
      return 13;
    case '=':
    case 'Y':
      return 14;
    case '?':
    case 'i':
      return 15;
    case '7':
    case 'L':
    case 'T':
    case 'l':
      return 16;
    case '*':
    case 'c':
    case 'u':
    case 't':
      return 17;
    case 'X':
    case '[':
    case ']':
    case 'n':
    case '{':
    case '}':
    case 'f':
    case 'I':
    case 'J':
      return 18;
    case '1':
    case 'w':
    case 'V':
    case 'z':
      return 19;
    case 'C':
    case 'o':
    case 'F':
    case 'j':
      return 20;
    case '4':
    case 'h':
    case 'K':
    case 's':
    case 'k':
      return 21;
    case '%':
    case 'm':
    case '0':
    case 'Z':
    case '2':
      return 22;
    case '3':
    case '8':
    case 'P':
    case 'e':
    case 'U':
    case 'a':
      return 23;
    case '#':
    case '&':
    case 'y':
    case 'A':
      return 24;
    case 'G':
    case 'H':
    case 'N':
    case 'b':
    case 'd':
    case 'p':
    case 'S':
    case 'q':
      return 25;
    case '6':
    case 'D':
    case 'W':
    case 'E':
    case '9':
    case 'O':
      return 26;
    case '5':
      return 27;
    case 'R':
    case 'M':
      return 28;
    case '$':
    case 'B':
      return 29;
    case 'g':
      return 30;
    case 'Q':
      return 31;
    case '@':
      return 32;
  }
}

int main(){
  string line;
  int total;
  while(getline(cin, line))
  {
    total = 0;
    for(int i = 0; i < line.length(); i++)
      total += getVal(line[i]);
    cout << total << endl;
  }
  return 0;
}
