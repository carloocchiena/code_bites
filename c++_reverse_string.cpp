#include <iostream>
using namespace std;

// Define is_palindrome() here:
bool is_palindrome(string text) {
  
  string reversed_text = "";
  
  for (int i = text.size() - 1; i >= 0; i--) {
    reversed_text += text[i];
  }
  
  if (reversed_text == text) {
    return true;
  }
  
  return false;
  
}

int main() {
  
  cout << is_palindrome("madam") << "\n";
  cout << is_palindrome("ada") << "\n";
  cout << is_palindrome("lovelace") << "\n";
  
}
