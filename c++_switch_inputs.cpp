#include <iostream>
using namespace std;

int main() {

double weight;
int planet_id;
string planet = "Earth";

std::cout << "What's your weight (kg)?\n";
std::cin >> weight;

std::cout << "Which planet are you visiting?\n";
std::cin >> planet_id;

switch (planet_id) {
  case 1:
  weight = weight * 0.38;
  planet = "Mercury";
  case 2:
  weight = weight * 0.91;
  planet = "Venus";
  case 3:
  weight = weight * 0.38;
  planet = "Mars";
  case 4:
  weight = weight * 2.34;
  planet = "Jupiter";
  case 5:
  weight = weight * 1.06;
  planet = "Saturn";
  case 6:
  weight = weight * 0.92;
  planet = "Uranus";
  case 7:
  weight = weight * 1.19;
  planet = "Neptune";
  default:
  std:cout << "\n";
} 
  
std::cout << "Your weight on " << planet << " would be " << weight << " kg\n";

return 0;  
  
}
