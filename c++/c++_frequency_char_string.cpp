#include <iostream>
using namespace std;

int main()
{
    string str = "C++ Programming is cool";
    char checkCharacter = 'a';
    int count = 0;

    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] ==  checkCharacter)
        {
            ++ count;
        }
    }

    cout << "Number of " << checkCharacter << " = " << count;

    return 0;
}
