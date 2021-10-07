#include<iostream>
#include<vector>

int main() {

  std::vector<int> nums = {2, 4, 3, 6, 1, 9};
  int odd = 1;
  int even = 0;

  for (int i = 0; i < nums.size(); i++) {
    if (i % 2 == 0) {
      even += nums[i];
    } else {
      odd = odd * nums[i];
    }
  } 

std::cout << "Sum of even numbers is " << even << "\n";
std::cout << "Product of odd numbers is " << odd << "\n";

}
